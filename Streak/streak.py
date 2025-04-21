import json
import time
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)


def kogama_login(session, user):
    print(f"Logging in as {user['login']}")
    res = session.post(
        "https://www.kogama.com/auth/login/",
        json={"username": user["login"], "password": user["password"]},
    )
    print(f"Login response status: {res.status_code}")
    return res


def kogama_logout(session):
    print("Logging out")
    res = session.get("https://www.kogama.com/auth/logout/")
    print(f"Logout response status: {res.status_code}")
    return res


def kogama_send_dm(session, sender_id, to_id, message):
    print(f"Sending DM from {sender_id} to {to_id} with message: {message}")
    res = session.post(
        f"https://www.kogama.com/chat/{sender_id}/",
        json={"to_profile_id": to_id, "message": message + "\n"},
    )

    if res.status_code in (200, 201):
        print(f"DM successfully sent from {sender_id} to {to_id}.")
    else:
        print(f"Failed to send DM from {sender_id} to {to_id}. Response: {res.text}")
        print(f"Response Status Code: {res.status_code}")
        print(f"Response Content: {res.text}")
    return res


session = requests.Session()
session.verify = False

main = config["mainaccount"]
bot = config["botaccount"]


res = kogama_login(session, main)
if res.status_code != 200:
    print(f"Failed to log in to main account: {res.text}")
    exit()


print("\nSending message from Main account to Bot account...")
res = kogama_send_dm(session, main["userID"], bot["userID"], main["message"])
if res.status_code not in (200, 201):
    print(f"Failed to send message from main account to bot account: {res.text}")
    exit()


res = kogama_logout(session)
time.sleep(0.6)


res = kogama_login(session, bot)
if res.status_code != 200:
    print(f"Failed to log in to bot account: {res.text}")
    exit()


print("\nSending message from Bot account to Main account...")
res = kogama_send_dm(session, bot["userID"], main["userID"], bot["message"])
if res.status_code not in (200, 201):
    print(f"Failed to send message from bot account to main account: {res.text}")
    exit()


res = kogama_logout(session)

print(
    "\nDue to this script using your own IPv4 (local session), you are required to log in again to your account from your browser. Sorry for the inconvenience!"
)
