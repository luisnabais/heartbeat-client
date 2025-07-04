import requests
import time
import socket
import os

SERVER_HOST = os.getenv("HEARTBEAT_SERVER_HOST", "localhost")
SERVER_PORT = os.getenv("HEARTBEAT_SERVER_PORT", "5001")
CLIENT_ID = os.getenv("HEARTBEAT_CLIENT_ID", socket.gethostname())
HEARTBEAT_INTERVAL = int(os.getenv("HEARTBEAT_INTERVAL", "120"))

SERVER_URL = f"http://{SERVER_HOST}:{SERVER_PORT}/heartbeat"

print(f"[INFO] Heartbeat client started as '{CLIENT_ID}', sending to {SERVER_URL} every {HEARTBEAT_INTERVAL}s.")

while True:
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    try:
        response = requests.post(SERVER_URL, json={"client_id": CLIENT_ID}, timeout=5)
        if response.status_code == 200:
            print(f"[{timestamp}] [OK] Heartbeat sent to {SERVER_URL} as '{CLIENT_ID}'")
        else:
            print(f"[{timestamp}] [ERROR] Unexpected response: {response.status_code} while sending heartbeat to '{CLIENT_ID}'")
    except Exception as e:
        print(f"[{timestamp}] [EXCEPTION] Failed to send heartbeat to {SERVER_URL} as '{CLIENT_ID}': {e}")
    time.sleep(HEARTBEAT_INTERVAL)
