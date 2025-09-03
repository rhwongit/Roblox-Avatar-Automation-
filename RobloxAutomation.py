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
    1012345678901234: "Chill Vibes",
    2023456789012345: "Street Style",
    3034567890123456: "Classic Cool",
    4045678901234567: "Urban Explorer",
    5056789012345678: "Night Rider",
    6067890123456789: "Summer Breeze"
}

# -----------------------------
# 4️⃣ Wear Outfit Function
# -----------------------------
def wear_outfit(outfit_id, name):
    wear_url = f"https://avatar.roblox.com/v1/outfits/{outfit_id}/wear"

    try:
        r = requests.post(wear_url, headers=HEADERS)

        # Handle CSRF token if 403
        if r.status_code == 403 and 'X-CSRF-TOKEN' in r.headers:
            HEADERS['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']
            r = requests.post(wear_url, headers=HEADERS)

        if r.status_code == 200:
            print(f"✅ Wore outfit: {name} (ID: {outfit_id})")
        else:
            print(f"❌ Failed to wear outfit: {name} (status {r.status_code})")
            print("Response:", r.text)
    except Exception as e:
        print(f"⚠️ Error wearing outfit '{name}': {e}")

# -----------------------------
# 5️⃣ Main Loop (Random Outfit Every Hour)
# -----------------------------
while True:
    outfit_id, name = random.choice(list(OUTFITS.items()))
    wear_outfit(outfit_id, name)
    print("⏳ Waiting 1 hour before next outfit...\n")
    time.sleep(3600)  # Wait 1 hour
