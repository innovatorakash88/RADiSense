import firebase_admin
from firebase_admin import credentials, db
import random
from datetime import datetime
import json
import os

# -------- FIREBASE AUTH FROM ENV --------
firebase_key = json.loads(os.environ["FIREBASE_KEY"])
cred = credentials.Certificate(firebase_key)

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://radisense-8829-default-rtdb.firebaseio.com"
})

# -------- GET LAST VALUES (optional) --------
ref_current = db.reference("current")
last_data = ref_current.get()

radiation = last_data["radiation_uSv_h"] if last_data else 0.15
battery = last_data["battery_percent"] if last_data else 100

# -------- SIMULATION --------
def simulate_radiation(value):
    change = random.uniform(-0.05, 0.2)
    if random.random() < 0.05:
        change += random.uniform(5, 20)
    return round(max(0.05, value + change), 3)

def get_status(val):
    if val < 0.3:
        return "SAFE", False
    elif val < 1.0:
        return "ELEVATED", False
    elif val < 5.0:
        return "MODERATE", False
    elif val < 20.0:
        return "HIGH", True
    else:
        return "EXTREME", True

radiation = simulate_radiation(radiation)
battery -= random.randint(1, 3)
if battery <= 0:
    battery = 100

status, alarm = get_status(radiation)
timestamp = datetime.utcnow().isoformat()

data = {
    "radiation_uSv_h": radiation,
    "status": status,
    "alarm": alarm,
    "battery_percent": battery,
    "timestamp": timestamp
}

# -------- PUSH TO FIREBASE --------
ref_current.set(data)
db.reference("history").push(data)

print("RADiSense update sent:", data)
