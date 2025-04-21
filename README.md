# KoGaMaStreak
A bad code script in python to boost your DMStreak locally without relying on another people xd <br>
Automatically log ins on an account, dms your bot account, logs out and answers from within bot account. <br>
***MAKE SURE TO HAVE YOUR BOTACCOUNT ADDED***, this script does NOT look through friend requests, lol.

```bash
# New Dir
mkdir streak
cd streak

# Virtual Env
python3 -m venv venv
source venv/bin/activate

# Reqs setup
pip install requests urllib3

# Create/edit config
cat > config.json <<EOF
{
    "mainaccount": {
      "userID": 111111,
      "login": "AccountToBoost",
      "password": "Password",
      "message": "Boost!"
    },
    "botaccount": {
      "userID": 111111,
      "login": "UselessAccount",
      "password": "Password",
      "message": "Boosting!"
    }
  }
EOF

# run
python3 streak.py
```

