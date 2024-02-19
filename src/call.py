import subprocess
import time

server = subprocess.Popen(["python3", "-m", "http.server", "[port]", "-d", "~/empty"])
time.sleep(60)
server.terminate()
