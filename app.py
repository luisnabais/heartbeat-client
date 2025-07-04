import requests
import time
import socket
import os

SERVER_HOST = os.getenv("HEARTBEAT_SERVER_HOST", "localhost")
SERVER_PORT = os.getenv("HEARTBEAT_SERVER_PORT", "5001")
CLIENT_ID = os.getenv("HEARTBEAT_CLIENT_ID", socket.gethostname())
HEARTBEAT_INTERVAL = int(os.getenv("HEARTBEAT_INTERVAL", "120"))

SERVER_URL = f"http://{SERVER_HOST}:{SERVER_PORT}/heartbeat"

print(f"[INFO] Heartbeat client iniciado como '{CLIENT_ID}', a enviar para {SERVER_URL} a cada {HEARTBEAT_INTERVAL}s.")

while True:
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    try:
        response = requests.post(SERVER_URL, json={"client_id": CLIENT_ID}, timeout=5)
        if response.status_code == 200:
            print(f"[{timestamp}] [OK] Heartbeat enviado para {SERVER_URL} como '{CLIENT_ID}'")
        else:
            print(f"[{timestamp}] [ERRO] Resposta inesperada: {response.status_code} ao enviar heartbeat para '{CLIENT_ID}'")
    except Exception as e:
        print(f"[{timestamp}] [FALHA] Falha ao enviar heartbeat para {SERVER_URL} como '{CLIENT_ID}': {e}")
    time.sleep(HEARTBEAT_INTERVAL)
