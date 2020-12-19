# scriptjacker
This is Scriptjacker, a payload encoding and delivery system. Scriptjacker generates a malware dropper that, when clicked, connects back to the attacker's machine for
code execution. Scriptjacker encodes the payload delivery service as a JSON web server. It clogs the JSON response with junk. However, it also sneaks in a Python Code object that
the client can then reconstruct and execute. Then, the code is executed. I am currently working on a way to package PIP dependencies.
