# 🎭 Roblox Avatar Automation

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python)](https://www.python.org/) 
[![Requests](https://img.shields.io/badge/Library-requests-green.svg)](https://pypi.org/project/requests/) 
[![Roblox](https://img.shields.io/badge/Platform-Roblox-red.svg?logo=roblox)](https://www.roblox.com)

Automate your Roblox avatar with Python! This script **cycles through your saved outfits**, handles errors automatically, and only wears outfits that are truly wearable.

---

## ✨ Features

- 🔐 Secure login using your `.ROBLOSECURITY` cookie
- 👕 Automatically cycle through editable outfits
- ⚡ Skips outfits that fail to wear and logs failures
- 📄 Generates `failed_outfits.log` with all outfits that couldn’t be worn
- ⏱️ Adjustable interval (default: 10 minutes)
- 💻 Cross-platform: Windows, Linux, macOS

---

## 🖼️ Sample Output

**Console Output:**

✅ Logged in as: TERMINATORR60 (UserId: 4755568233)
✨ Found 8 editable outfits.
✅ Wore outfit: Supreme (ID: 3213680585124979)
⚠️ Could not wear outfit 'Tokyo 10' (ID: 2721320690592434, status 404)
⏳ Waiting 10 minutes before next outfit...


**Failed Outfits Log (`failed_outfits.log`):**

Tue Sep 3 13:45:12 2025 - Failed to wear: Tokyo 10 (ID: 2721320690592434), Status: 404
Tue Sep 3 13:55:18 2025 - Failed to wear: BPM Black (ID: 2719305988962447), Status: 404


**Sample Avatar Image Placeholder:**

![Sample Avatar](https://via.placeholder.com/300x300.png?text=Avatar+Preview)

---

## 🛠️ Tech Stack

- Python 3.x
- `requests` library
- Roblox platform

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/roblox-avatar-automation.git
cd roblox-avatar-automation

# Install dependencies
pip install requests

🔑 Setup
Step 1 — Get Your Roblox Cookie

    Open Roblox and log in.

    Press F12 (Developer Tools) → Network tab.

    Refresh the page and click any request to roblox.com.

    Under Request Headers, find:

Cookie: .ROBLOSECURITY=YOUR_COOKIE_HERE

    Copy everything after = and save it into a file called cookie.txt in the project root.

    ⚠️ Keep this cookie private — leaking it can compromise your account.

Step 2 — Run the Script

python avatar_automation.py

The script will:

    ✅ Log in with your cookie

    👕 Cycle through your editable outfits automatically

    ⚠️ Skip any outfits that cannot be worn and log them in failed_outfits.log

    ⏳ Wait 10 minutes before changing to the next outfit

Step 3 — Optional Configuration

    Change the interval in the script by modifying:

time.sleep(600)  # Interval in seconds (600 = 10 minutes)

    Check failed_outfits.log to remove problematic outfits from rotation.

🎨 Customization

    Add or remove outfits by editing OUTFITS dictionary (optional if using auto-fetch)

    Extend with more features like random order, notifications, or web UI integration

🤝 Contributing

Contributions are welcome!

    Fork this repository

    Create a feature branch (git checkout -b feature-name)

    Commit your changes (git commit -m 'Add feature')

    Push to the branch (git push origin feature-name)

    Open a pull request
