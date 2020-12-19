def f():
    exec('''import subprocess as sp
sp.run("ncat localhost 22 -e cmder")
print("ABCD")
''')