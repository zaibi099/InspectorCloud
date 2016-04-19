#!/usr/bin/env python
import re
from Authentication import *
from MongoDatabase import *

class BillGeneratePreReq:

    def __init__(self):

        self.aObj = Authentication("yess");
        self.nova = self.aObj.getComputeClient();
        self.neutron = self.aObj.getNeutronClient();
        self.keystone= self.aObj.getKeystoneClient();
        self.glance = self.aObj.getGlanceClient();
        self.cclient = self.aObj.getCeilometerClient();
        self.dbObj = MongoDatabase();

    def getAllBillsCategories(self):

    	checki = self.dbObj.getAllBillCat();
    	if(checki==False):
    		return False
    	else:
    		return checki;

    def getAllRunningInstances(self):

    	servers = self.nova.servers.list();
    	return servers;

# obj = BillGeneratePreReq();
# obj.getAllBillsCategories();