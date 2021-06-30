__author__    = "Nelson Murilo"
__email__     = "nmurilo@gmail.com"
_copyright__ = "Copyright (c) 2011-2021 Pangeia"
__license__   = "AMS"
__version__   = "0.2"
__date__      = "2021-06-29"
import os
import sys
from sys import platform 
import subprocess 

try:
   url = sys.argv[1]
except:
   print ("\nUsage: python sslcheck.py host [port]")
   quit()

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
            sub.terminate()
            break
      sub.terminate()
   except: 
      pass # ignore 
