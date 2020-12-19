import subprocess as sp
print("Creating netcat listener...")
sp.run("nc -lvnp 22",shell=True)
print("bai")