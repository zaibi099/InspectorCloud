#!/usr/bin/env python
import sys
from Router import *

args=[];

for arg in sys.argv:
    args.append(arg);
    print arg

rtrObj = Router(args);
rtrObj.createRouter();