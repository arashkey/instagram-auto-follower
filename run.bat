@Echo off

if not exist "%PROGRAMFILES%\Mozilla Firefox\firefox.exe" start /wait "" "https://www.mozilla.org/en-US/firefox/all/"

 

:: Check for Python Installation
py --version 3>NUL
if errorlevel 1 goto errorNoPython
 
goto:runProject

:errorNoPython
echo Download and install Python 
start "" https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe

:runProject

set PATH=%PATH%;%appdata%\..\Local\Programs\Python\Python39\Scripts

echo after installing Python
call pip install instapy 
if errorlevel 1 goto eof

py insta.py 2>errorlog.txt
:eof
