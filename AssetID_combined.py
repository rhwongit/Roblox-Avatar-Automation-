import requests
import json

# -----------------------------
# 1️⃣ Load ROBLOSECURITY Cookie
# -----------------------------
with open("cookie.txt", "r") as f:
    COOKIE = f.read().strip()

HEADERS = {
    "Cookie": f".ROBLOSECURITY={COOKIE}",
    "Content-Type": "application/json"
}

# CSRF Token fetch
token_req = requests.post("https://auth.roblox.com/v1/logout", headers=HEADERS)
HEADERS["X-CSRF-TOKEN"] = token_req.headers.get("x-csrf-token")

# -----------------------------
# 2️⃣ Get authenticated user
# -----------------------------
resp = requests.get("https://users.roblox.com/v1/users/authenticated", headers=HEADERS)
if resp.status_code != 200:
    print("❌ Invalid cookie. Please update cookie.txt")
    exit()

user = resp.json()
print(f"✅ Logged in as: {user['name']} (UserId: {user['id']})")

# -----------------------------
# 3️⃣ User chooses avatar type
# -----------------------------
choice = input("Which avatar type to fetch? (R6 / R15 / Both): ").strip().upper()
if choice not in ["R6", "R15", "BOTH"]:
    print("❌ Invalid choice.")
    exit()

fetch_r6 = choice in ["R6", "BOTH"]
fetch_r15 = choice in ["R15", "BOTH"]

# -----------------------------
# 4️⃣ Fetch all editable outfits
# -----------------------------
outfits_url = f"https://avatar.roblox.com/v1/users/{user['id']}/outfits?itemsPerPage=50"
resp = requests.get(outfits_url, headers=HEADERS)

if resp.status_code != 200:
    print("❌ Failed to fetch outfits:", resp.status_code, resp.text)
    exit()

outfits_data = resp.json().get("data", [])

# Containers for filtered outfits
saved_outfits_r6 = {}
saved_outfits_r15 = {}

for outfit in outfits_data:
    if not outfit.get("isEditable", False):
        continue

    outfit_id = outfit["id"]
    outfit_name = outfit["name"]

    details_url = f"https://avatar.roblox.com/v1/outfits/{outfit_id}/details"
    details_resp = requests.get(details_url, headers=HEADERS)

    if details_resp.status_code != 200:
        print(f"⚠️ Could not fetch details for outfit '{outfit_name}'")
        continue

    details = details_resp.json()
    avatar_type = details.get("playerAvatarType", "R15")

    # Assign to proper container
    if avatar_type == "R6" and fetch_r6:
        saved_outfits_r6[outfit_name] = {
            "id": outfit_id,
            "assets": [item["id"] for item in details.get("assets", [])],
            "bodyColors": details.get("bodyColors", {}),
            "avatarType": "R6"
        }
    elif avatar_type == "R15" and fetch_r15:
        saved_outfits_r15[outfit_name] = {
            "id": outfit_id,
            "assets": [item["id"] for item in details.get("assets", [])],
            "bodyColors": details.get("bodyColors", {}),
            "avatarType": "R15"
        }

# -----------------------------
# 5️⃣ Save outfits to JSON/TXT
# -----------------------------
if fetch_r6:
    with open("outfits_r6.json", "w", encoding="utf-8") as f:
        json.dump(saved_outfits_r6, f, indent=4)
    with open("outfits_r6.txt", "w", encoding="utf-8") as f:
        for name, data in saved_outfits_r6.items():
            f.write(f"Outfit: {name} (ID: {data['id']})\n")
            f.write(f"  Assets: {', '.join(map(str, data['assets']))}\n")
            f.write(f"  AvatarType: {data['avatarType']}\n")
            f.write(f"  BodyColors: {data['bodyColors']}\n")
            f.write("-"*40 + "\n")
    print(f"✅ Saved {len(saved_outfits_r6)} R6 outfits to outfits_r6.json / .txt")

if fetch_r15:
    with open("outfits_r15.json", "w", encoding="utf-8") as f:
        json.dump(saved_outfits_r15, f, indent=4)
    with open("outfits_r15.txt", "w", encoding="utf-8") as f:
        for name, data in saved_outfits_r15.items():
            f.write(f"Outfit: {name} (ID: {data['id']})\n")
            f.write(f"  Assets: {', '.join(map(str, data['assets']))}\n")
            f.write(f"  AvatarType: {data['avatarType']}\n")
            f.write(f"  BodyColors: {data['bodyColors']}\n")
            f.write("-"*40 + "\n")
    print(f"✅ Saved {len(saved_outfits_r15)} R15 outfits to outfits_r15.json / .txt")
