import subprocess
# pretty simple, just run ncat
subprocess.run("ncat --listen localhost 22")
print("hai") # stop python from quitting