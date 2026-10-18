import json

import requests


def main():
    base_url = input("Classmate's Render base URL (https://...onrender.com): ").strip().rstrip("/")
    path = input("Classmate's endpoint path (for example, /courses): ").strip()
    if not base_url or not path:
        print("Both the Render base URL and endpoint path are required.")
        return
    if not path.startswith("/"):
        path = f"/{path}"

    try:
        response = requests.get(f"{base_url}{path}", timeout=30)
    except requests.RequestException as error:
        print(f"Request failed: {error}")
        return

    if response.status_code != 200:
        print("Request failed.")
        print("Status Code:", response.status_code)
        return

    try:
        data = response.json()
    except ValueError:
        print("The server response was not valid JSON.")
        print(response.text)
        return

    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()