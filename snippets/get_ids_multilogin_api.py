"""Multilogin X API helper: retrieve profiles, folders, workspace IDs."""

import os
import requests

BASE_URL = os.getenv("MULTILOGIN_API_URL", "http://127.0.0.1:35000")
API_TOKEN = os.getenv("MULTILOGIN_API_TOKEN", "")

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

if API_TOKEN:
    HEADERS["Authorization"] = f"Bearer {API_TOKEN}"


def get_profiles():
    url = f"{BASE_URL}/api/v2/browser_profiles"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.json()


def get_folders():
    url = f"{BASE_URL}/api/v2/folders"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.json()


def get_workspaces():
    url = f"{BASE_URL}/api/v2/workspaces"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    # fallback if endpoint differs (e.g., '/api/v2/teams')
    if resp.status_code == 404:
        url = f"{BASE_URL}/api/v2/teams"
        resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.json()


def get_users():
    url = f"{BASE_URL}/api/v2/users?limit=100&offset=0"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.json()


def get_current_user():
    url = f"{BASE_URL}/api/v2/user"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.json()


if __name__ == "__main__":
    print("Multilogin X API endpoint:", BASE_URL)

    print("\nProfiles:")
    try:
        profiles = get_profiles()
        for p in profiles.get("items", profiles if isinstance(profiles, list) else []):
            print(f"- profileId={p.get('id')} name={p.get('name')}")
    except Exception as e:
        print("Error retrieving profiles:", e)

    print("\nFolders:")
    try:
        folders = get_folders()
        for f in folders.get("items", folders if isinstance(folders, list) else []):
            print(f"- folderId={f.get('id')} name={f.get('name')} workspaceId={f.get('workspaceId')}")
    except Exception as e:
        print("Error retrieving folders:", e)

    print("\nWorkspaces:")
    try:
        workspaces = get_workspaces()
        for w in workspaces.get("items", workspaces if isinstance(workspaces, list) else []):
            print(f"- workspaceId={w.get('id')} name={w.get('name')}")
    except Exception as e:
        print("Error retrieving workspaces:", e)

    print("\nUsers:")
    try:
        users = get_users()
        for u in users.get("data", users.get("users", [])):
            print(f"- userId={u.get('user_id') or u.get('id')} email={u.get('email')}")
    except Exception as e:
        print("Error retrieving users:", e)

    print("\nCurrent user:")
    try:
        current = get_current_user()
        print(current)
    except Exception as e:
        print("Error retrieving current user:", e)
