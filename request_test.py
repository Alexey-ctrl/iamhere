import requests
import subprocess

subprocess.call("python server/app.py", shell=True)
print("1")
r = requests("localhost:5555")
print("2")
print(r)