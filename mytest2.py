'''
for x in "hello":
    print (x)
'''
import subprocess
import shlex
subprocess.call(shlex.split('./test.sh param1 param2'))