
# 🛠️ Quick Troubleshooting Checklist

Before asking for help, try these steps:

- [ ] Are you logged in with the correct account?
- [ ] Did you open the correct Network/Storage tab in DevTools?
- [ ] Did you reload the page after opening DevTools?
- [ ] Can't find token/ID? Try logging out and back in, or clear your browser cache.
- [ ] Did you check your API/token permissions?
- [ ] Did you try the sample scripts below?

If you still have issues, please open an issue with screenshots and the commands you tried.

# 📊 Comparison: Ways to Get Token/ID

| Method     | Pros                        | Cons                        | When to use?                |
| ---------- | --------------------------- | --------------------------- | --------------------------- |
| DevTools   | Fast, no extra install      | Manual, easy to miss a tab  | Quick one-time retrieval    |
| API        | Automatable, script-ready   | Needs token, rate limits    | Frequent/automated use      |
| CLI/Tool   | Workflow/batch integration  | Needs install, version bugs | Advanced/large-scale tasks  |
| UI         | Easy, no tech skills needed | Not automatable             | Beginners, quick checks     |

# 🧩 Template Scripts

Ready-to-use scripts—just replace your token/ID:

## Get user list via API
```python
import requests
API_URL = "http://localhost:35000/api/v2/users"
API_TOKEN = "<your_api_token>"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
response = requests.get(API_URL, headers=headers)
print(response.json())
```

## Get profile details
```python
import requests
API_URL = "http://localhost:35000/api/v2/profiles/<profile_id>"
API_TOKEN = "<your_api_token>"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
response = requests.get(API_URL, headers=headers)
print(response.json())
```

## Automatically get token from sessionStorage (Chrome, Playwright)
```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
	browser = p.chromium.launch(headless=False)
	page = browser.new_page()
	page.goto("https://app.multilogin.com")
	# Log in manually if needed
	token = page.evaluate("window.sessionStorage.getItem('token')")
	print("Token:", token)
	browser.close()
```

# 📚 Real-World Use Cases & FAQ

- **Can't find token/ID?** → Usually caused by not reloading the page or expired session.
- **API returns 401/403 error?** → Token is wrong/expired, try getting a new token.
- **Script runs but no result?** → Check endpoint, permissions, or try with another profile.

Found a new issue or useful tip? Please submit a PR or open an issue to help the community!

# 🚀 Partner Offers & Affiliate Discounts

**Get Multilogin with exclusive discounts!**

- 🔗 [Buy Multilogin with 50% OFF (ADBNEW50)](https://adblogin.com/go/multilogin) — Use code: `ADBNEW50`
- 🔗 [Buy Multilogin with 50% OFF (SAVE50)](https://adblogin.com/go/multilogin) — Use code: `SAVE50`

Share these codes with your team for the best deal on Multilogin.

# Quick solutions with Developer Tools

Quick solutions with Developer Tools: easy guides to access tokens, IDs, and key info for faster, smoother Multilogin setup and troubleshooting.

## Table of Contents

1. [Introduction](#introduction)
2. [Tutorials](#tutorials)
3. [Snippets](#snippets)
4. [How to Contribute](#how-to-contribute)
5. [SEO topics](#seo-topics)

## Introduction

This repository provides concise, step-by-step guides and automation snippets for Multilogin, focused on developer productivity and troubleshooting. All tutorials are in English, with images and code organized for easy reference.

## Tutorials

- `tutorials/how-to-get-profile-folder-workspace-ids-devtools.md`
- `tutorials/how-to-find-user-id-in-devtools.md`
- `tutorials/how-to-get-api-tokens-in-devtools.md`
- `tutorials/multilogin-x-api-overview.md`
- `tutorials/placeholder-3-missing-source.md`

## Snippets

- `snippets/get_ids_multilogin_api.py`

## How to Contribute

1. Add saved official Multilogin HTML under project root.
2. Convert content into `/tutorials` with Overview, Step-by-step, and Technical Tips.
3. Create matching `/snippets` Python/Playwright API automation loader.
4. Add SEO topics to this README.

## SEO topics

- Multilogin X API automation
- How to get Multilogin profile ID
- Multilogin folder ID API
- Multilogin workspace ID retrieval
- Multilogin DevTools instructions
- Python Multilogin API script
- Playwright Multilogin automation
- Multilogin CLI vs API
- Multilogin token management
- Multilogin web interface automation
- Multilogin folder synchronization
- Multilogin team workspace setup
- Multilogin profile cloning
- Multilogin session handling
- Multilogin error troubleshooting
- Multilogin upgrade guide
- Multilogin Docker automation
- Multilogin browser profile lifecycle
- Multilogin best practices
- Multilogin endpoint security

