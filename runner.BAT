cd /D "C:\Program Files (x86)\Google\Chrome\Application"
start chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"
cd /D "E:\OrKeren\program\dating"
call "venv\Scripts\activate"
py main.py