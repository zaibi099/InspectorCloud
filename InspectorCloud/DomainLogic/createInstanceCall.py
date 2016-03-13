#!/usr/bin/env python
from instanceCreate import *

args=[None]*7;
itr=0;

for arg in sys.argv:
	print arg;
	args[itr]=arg;
	itr=itr+1;

instanceObj = InstanceCreate(args);
instanceObj.createInstance();

instanceObj.addSecurityGroups();
instanceObj.assignFloatingIp();