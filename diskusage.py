#!/usr/bin/env python

import os
import sys 
 
files = os.listdir(sys.argv[1])
  
for x in files:
  fullpath = sys.argv[1] + "/" + x
  hrfilesize = os.path.getsize(fullpath) / 1024
  print (fullpath,hrfilesize) 


