import os
import sys
from sys import platform 
import subprocess 

url = sys.argv[1]
port="443"
if len(sys.argv) == 3: 
    port = sys.argv[2]

out = os.popen("openssl ciphers ALL").read().split(':') 
print("Accepting: ")

for c in out:
   cmd = "openssl s_client -connect "+url+":"+port+" -cipher "+c
   sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
   try:
      #print("Testing... "+c)  # debug 
      for ln in iter(sub.stdout.readline, b' '): 
         line = str(ln) 
         if "Error" in line: 
            sub.terminate()
            break
         if "(NONE)" in line:
            sub.terminate()
            break
         if "Cipher " in line: 
            if platform == "win32": 
               print(line[6:-5])
            else:
               print(line[6:-3])
            subterminate()
            break
      sub.terminate()
   except: 
      pass # ignore 
