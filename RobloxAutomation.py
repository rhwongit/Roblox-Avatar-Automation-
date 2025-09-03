import requests
import time
import random

# -----------------------------
# 1️⃣ Load ROBLOSECURITY Cookie
# -----------------------------
with open("cookie.txt", "r") as f:
    COOKIE = f.read().strip()

HEADERS = {
    "Cookie": f".ROBLOSECURITY={COOKIE}",
    "Content-Type": "application/json"
}

# -----------------------------
# 2️⃣ Validate Cookie
# -----------------------------
resp = requests.get("https://users.roblox.com/v1/users/authenticated", headers=HEADERS)
if resp.status_code != 200:
    print("❌ Cookie invalid or expired. Please update your cookie.")
    exit()

user = resp.json()
print(f"✅ Logged in as: {user['name']} (UserId: {user['id']})")

# -----------------------------
# 3️⃣ Outfit List
# -----------------------------
OUTFITS = {
    3213680585124979: "Supreme",
    2721320690592434: "Tokyo 10",
    3233427509340402: "Sweat Track",
    958531658965714: "BPM Blue",
    2719305988962447: "BPM Black",
    4004004853720826: "Malbro"
}

# -----------------------------
# 4️⃣ Wear Outfit Function
# -----------------------------
def wear_outfit(outfit_id, name):
    try:
        # Fetch outfit details
        details_url = f"https://avatar.roblox.com/v1/outfits/{outfit_id}/details"
        r = requests.get(details_url, headers=HEADERS)
        if r.status_code != 200:
            print(f"❌ Could not fetch outfit '{name}' (ID: {outfit_id}, status {r.status_code})")
            return

        asset_ids = [item["id"] for item in r.json()["assets"]]

        # POST to set assets (handle CSRF)
        wear_url = "https://avatar.roblox.com/v1/avatar/set-wearing-assets"
        r2 = requests.post(wear_url, headers=HEADERS, json={"assets": asset_ids})

        if r2.status_code == 403 and "X-CSRF-TOKEN" in r2.headers:
            HEADERS["X-CSRF-TOKEN"] = r2.headers["X-CSRF-TOKEN"]
            r2 = requests.post(wear_url, headers=HEADERS, json={"assets": asset_ids})

        if r2.status_code == 200:
            print(f"✅ Wore outfit: {name} (ID: {outfit_id})")
        else:
            print(f"❌ Failed to wear outfit '{name}' (ID: {outfit_id}, status {r2.status_code})")
            print("Response:", r2.text)
    except Exception as e:
        print(f"⚠️ Error wearing outfit '{name}': {e}")

# -----------------------------
# 5️⃣ Main Loop (Every Hour)
# -----------------------------
while True:
    outfit_id, name = random.choice(list(OUTFITS.items()))
    wear_outfit(outfit_id, name)
    print("⏳ Waiting 1 hour before next outfit...\n")
    time.sleep(3600)  # 1 hour
