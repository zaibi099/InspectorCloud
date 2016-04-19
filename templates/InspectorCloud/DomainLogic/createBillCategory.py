#!/usr/bin/env python
from Authentication import *
from MongoDatabase import *
import itertools

class createBillCategory:

	def __init__(self,billName,flvr,price):

		self.aObj = Authentication("yess");
		self.nova = self.aObj.getComputeClient();
		self.neutron = self.aObj.getNeutronClient();
		self.keystone= self.aObj.getKeystoneClient();
		self.glance = self.aObj.getGlanceClient();
		self.cclient = self.aObj.getCeilometerClient();
		self.price=price;
		self.billName=billName;
		self.flvrNames=flvr;
		self.dbObj = MongoDatabase();

	def saveBillCategory(self):

		dicti={};
		
		try:

			for f,b in zip(self.flvrNames,self.price):
				f = f.replace(".","\uff0e");
				dicti[f]=b
		
		except:
			print 'exception..'
		
		store={"name":self.billName,"type":"flvr_based","priceList":dicti};
		print store;
		self.addToDatabase(store);

	def addToDatabase(self,data):
		self.dbObj.addBillCategory(data);


# prici={ "m1\\uff0elarge":"50","m1\\uff0esmall":"60","m1\\uff0emini":"70","m1\\uff0exlarge":"80","m1\\uff0etiny":"90" }
# obj = createBillCategory("niki_minhaj","flvr_based",prici);
# obj.saveBillCategory();