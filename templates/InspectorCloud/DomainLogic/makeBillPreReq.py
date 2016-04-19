#!/usr/bin/env python
import sys
import re
from Authentication import *


class makeBillPreReq:
    
    def __init__(self):

        self.aObj = Authentication("yess");
        self.nova = self.aObj.getComputeClient();
        self.neutron = self.aObj.getNeutronClient();
        self.keystone = self.aObj.getKeystoneClient();
        self.glance = self.aObj.getGlanceClient();
        self.cclient = self.aObj.getCeilometerClient();
    
    def getAllFlavours(self):

        return self.nova.flavors.list();

    def getMyFlavourDetails(self,flvrName):

	    flvrs = self.nova.flavors.list();

	    for each in flvrs:
	    	if (each.name==flvrName):
	    		return each;

		return None;
