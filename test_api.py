import requests

BASE_URL = "https://siriregonda-content-env.hf.space"

# Step 1: Reset environment
reset = requests.get(f"{BASE_URL}/reset")
print("RESET:", reset.json())

# Step 2: Take an action
response = requests.post(f"{BASE_URL}/step", json={
    "action": "post_reel"
})

print("STEP:", response.json())
