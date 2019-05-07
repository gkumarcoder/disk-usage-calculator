#!/usr/bin/env python

import os
import sys 
 
files = os.listdir(sys.argv[1])
for x in files:
  fullpath = sys.argv[1] + "/" + x
  hrfilesize = os.path.getsize(fullpath) / 1024
  
  print (fullpath,hrfilesize) 
  
 import subprocess
 threshold = 10
 child = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
 output = child.communicate()[0].strip().split("\n")
 for x in output[1:]:
            if int(x.split()[-2][:-1]) >= threshold:
            print x


