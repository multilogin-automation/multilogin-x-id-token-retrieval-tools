# Multilogin X API Overview

This guide provides a concise overview of the Multilogin X API, including authentication, endpoints, request/response formats, and error handling. Use this as a reference for automating Multilogin X with scripts and bots.

---

## What is the Multilogin X API?
The Multilogin X API allows you to programmatically manage browser profiles, automate profile actions, and retrieve usage data. It is designed for developers and automation engineers who want to integrate Multilogin X into their workflows.

---


## Authentication
- **Bearer Token:** Most API requests require a Bearer Token for authentication.
- **How to Get a Token:**
  - Sign in to the Multilogin X web app and extract the token from session storage (see the API token tutorial).
  - Tokens are valid for 30 minutes. Refresh with `POST /user/refresh_token`.
  - For higher rate limits and longer token lifetimes, use an automation token.

> **💡 Partner Offer:**
> Get 50% OFF Multilogin with code `ADBNEW50` or `SAVE50`
> 👉 [Buy with discount](https://adblogin.com/go/multilogin)

---

## Endpoints Overview
- **Base URL:** `https://api.multilogin.com`
- **Categories:**
  - **Launcher:** Start, stop, and get info about browser profiles.
  - **Profile Management:** Create, update, and delete browser profiles.
  - **Profile Access Management:** Sign in, manage passwords/tokens, get workspace info.
  - **Browser Profile Data:** Unlock browser profiles, retrieve usage/activity data.

---

## Request and Response Format
- **Requests:** JSON-formatted.
- **Responses:** JSON-formatted.
- **Example Request:**

```http
GET /api/v2/profiles HTTP/1.1
Host: api.multilogin.com
Authorization: Bearer <your_token>
Content-Type: application/json
```

---

## Error Handling
- **HTTP Status Codes:**
  - `2xx`: Success
  - `4xx`: Client error (invalid parameters, unauthorized, etc.)
  - `5xx`: Server error (internal error, service unavailable, etc.)
- **Error Responses:** Include error messages for troubleshooting.

---

## Example: Get All Profiles (Python)

```python
import requests

API_URL = "https://api.multilogin.com/api/v2/profiles"
API_TOKEN = "<your_api_token>"

headers = {"Authorization": f"Bearer {API_TOKEN}"}
response = requests.get(API_URL, headers=headers)

if response.ok:
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")
```

---

## Resources
- [Official API Documentation](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)
- [Support Page](https://help.multilogin.com/en_US/multilogin-x)

For more automation tips and code examples, see other tutorials in this handbook.
