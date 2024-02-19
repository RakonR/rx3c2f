# rx3c2f

[![Visit rakon.tech](https://img.shields.io/badge/Visit-rakon.tech-blue)](https://rakon.tech)

## Overview

rx3c2f (rx3's Command and Control Framework) is my first GitHub repo. It is a C2 framework designed for managing and controlling remote systems.

## Features

- **FUD:** Fully undetecatble on Windows Defender.
- **Reverse shell:** Administrator level shell.
- **Keylogging:** Logs stored in C:\Users\Public\Documents\
- **Persistance:** Zombies stay infected after reboot, and you can respawn your shell in case it dies.

## Tested on

**Servers:**
- Kali
- Raspbian
- Parrot OS
  
**Clients:**
- Windows 10
- Windows 11

### Installation

   ```bash
   git clone https://github.com/Rakon/rx3c2f.git
   cd rx3c2f
   python3 setup.py
