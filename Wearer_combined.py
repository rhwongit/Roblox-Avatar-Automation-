import requests
import time
import random
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
# 2️⃣ User chooses avatar type to wear
# -----------------------------
choice = input("Which avatar type to wear? (R6 / R15 / Both): ").strip().upper()
if choice not in ["R6", "R15", "BOTH"]:
    print("❌ Invalid choice.")
    exit()

wear_r6 = choice in ["R6", "BOTH"]
wear_r15 = choice in ["R15", "BOTH"]

# -----------------------------
# 3️⃣ Load outfits
# -----------------------------
OUTFITS = {}
if wear_r6:
    with open("outfits_r6.json", "r", encoding="utf-8") as f:
        OUTFITS.update(json.load(f))
if wear_r15:
    with open("outfits_r15.json", "r", encoding="utf-8") as f:
        OUTFITS.update(json.load(f))

if not OUTFITS:
    print("❌ No outfits found for the selected type(s). Run logger first.")
    exit()

# -----------------------------
# 4️⃣ Wear outfit function
# -----------------------------
def wear_outfit(name, data):
    payload = {
        "assetIds": data["assets"],
        "bodyColors": data.get("bodyColors", {}),
        "playerAvatarType": data["avatarType"]
    }

    url = "https://avatar.roblox.com/v1/avatar/set-wearing-assets"

    try:
        r = requests.post(url, headers=HEADERS, json=payload)

        # Handle CSRF token
        if r.status_code == 403:
            token = r.headers.get('X-CSRF-TOKEN')
            if token:
                HEADERS['X-CSRF-TOKEN'] = token
                r = requests.post(url, headers=HEADERS, json=payload)

        if r.status_code == 200:
            print(f"✅ Wore outfit: {name} ({data['avatarType']})")
        else:
            print(f"⚠️ Failed to wear {name}: {r.status_code} {r.text}")

    except Exception as e:
        print(f"⚠️ Error wearing {name}: {e}")

# -----------------------------
# 5️⃣ Main loop: random outfit every 10 minutes
# -----------------------------
while True:
    name, data = random.choice(list(OUTFITS.items()))
    wear_outfit(name, data)
    print("⏳ Waiting 30 minutes before next outfit...\n")
    time.sleep(1800)  # 30 minutes
