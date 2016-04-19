import sys
from Authentication import *

class InstanceBill:

	def __init__(self,instnc,catg):

		self.aObj = Authentication("yess");
		self.nova = self.aObj.getComputeClient();
		self.neutron = self.aObj.getNeutronClient();
		self.keystone= self.aObj.getKeystoneClient();
		self.glance = self.aObj.getGlanceClient();
		self.cclient = self.aObj.getCeilometerClient();
		self.inst = instnc;
		slef.catg = catg;

	def getInstanceID(self):

		instanceList = nova.servers.list(search_opts={'all_tenants': 1});

		for i in range(0,len(instanceList),1):
			if(instanceList[i].name==self.inst):
		    	return instncID = instanceList[i].id;

	def getTopSamples(self):

		