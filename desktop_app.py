
import subprocess
import time
import webview
import os
import sys
import urllib.request

# Project folder
project_folder = os.path.dirname(os.path.abspath(__file__))

# Start Streamlit in the background without showing CMD
startup_info = subprocess.STARTUPINFO()
startup_info.dwFlags |= subprocess.STARTF_USESHOWWINDOW

server = subprocess.Popen(
    [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        os.path.join(project_folder, "app.py"),
        "--server.headless=true",
        "--server.port=8501"
    ],
    cwd=project_folder,
    startupinfo=startup_info,
    creationflags=subprocess.CREATE_NO_WINDOW
)

# Wait for Streamlit to start
for attempt in range(30):
    try:
        urllib.request.urlopen("http://localhost:8501")
        break
    except Exception:
        time.sleep(1)

# Open the chatbot in a desktop window
try:
    webview.create_window(
        "ALI KARYANA STORE",
        "http://localhost:8501",
        width=1100,
        height=750
    )
    webview.start()
finally:
    server.terminate()
