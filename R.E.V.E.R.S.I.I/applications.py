import threading
import subprocess
import webbrowser

x=lambda: webbrowser.open_new("http://google.com")
t=threading.Thread(target=x)
t.start()

subprocess.Popen("C:\\windows\\System32\\calc.exe")