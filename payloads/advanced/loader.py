# This is a helper module that creates a payload ready to be used by scriptjacker to install seperate dependencies on the system. THESE MODULES REQUIRE A SYSTEM PYTHON,
# YOU MIGHT WANT TO CONSIDER INSTALLING PYTHON ON THE TARGET SYSTEM AFTER YOU HAVE GAINED A BASIC SHELL, THEN USING THESE TOOLS TO FURTHER PWN THE SYSTEM
import sys
import json
module=sys.argv[1]
with open(module+"/loader.json") as f: y=json.load(f)
deps=y["deps"]
depfile=[x+"\n" for x in deps]