import requests
import time

# Read cookie from file
with open("cookie.txt", "r") as f:
    COOKIE = f.read().strip()

# Headers for Roblox API
HEADERS = {
    "Cookie": f".ROBLOSECURITY={COOKIE}"
}

# Endpoint to validate cookie
CHECK_COOKIE_URL = "https://users.roblox.com/v1/users/authenticated"

# Outfits you want to cycle through (replace with your Outfit IDs)
OUTFITS = [ 123456, 0987654 ] 

# Validate cookie
resp = requests.get(CHECK_COOKIE_URL, headers=HEADERS)
if resp.status_code != 200:
    print("❌ Cookie invalid or expired. Please update cookie.txt")
    exit()

user = resp.json()
print(f"✅ Logged in as: {user['name']} (UserId: {user['id']})")

# Function to wear an outfit
def wear_outfit(outfit_id):
    url = f"https://avatar.roblox.com/v1/outfits/{outfit_id}/wear"
    r = requests.post(url, headers=HEADERS)
    if r.status_code == 200:
        print(f"✅ Changed outfit to {outfit_id}")
    else:
        print(f"❌ Failed to change outfit {outfit_id} (status {r.status_code})")
        print("Response:", r.text)

# Loop every hour
while True:
    for outfit_id in OUTFITS:
        wear_outfit(outfit_id)
        print("⏳ Waiting 1 hour...\n")
        time.sleep(3600)  # 1 hour
