# RADiSense – Radioactivity Detection

RADiSense is a project to monitor radiation levels using a dashboard.

The project shows:
- Radiation level
- Battery level of detector
- Alarm status
- Radiation history

## How it works

- Python code is used to **simulate radiation values**
- The Python simulator sends data to **Firebase Realtime Database**
- Firebase stores the data
- The dashboard reads data from Firebase and displays it

## Radiation Levels

The simulator shows different conditions:
- Safe
- Moderate (low radiation, may have side effects)
- Danger / Extreme

Alarm:
- Alarm is OFF in Safe and Moderate
- Alarm turns ON only in Danger level

## Battery Simulation

- Battery level decreases slowly
- When battery reaches 0%, it recharges again
- Battery behavior is realistic

## Dashboard

- Shows live radiation values
- Shows battery percentage
- Shows alarm status
- Shows radiation history
- History is not deleted and always remains

## Important Note

- Python simulator **does NOT run automatically**
- It runs only when the Python file is executed
- Firebase cannot run Python code
- If Python is not running, dashboard will show last stored values

## Technologies Used

- Python (for simulation logic)
- Firebase Realtime Database
- Dashboard built using Lovable

## Current Status

- Dashboard is working correctly
- Firebase is connected
- Simulator works when run manually

## Future Plans

- Run simulator on cloud without laptop
- Connect real radiation sensor hardware

- ## License

© 2026 RADiSense

This project is licensed under the MIT License.
See the LICENSE file for details.

- Cloud execution is not enabled yet
