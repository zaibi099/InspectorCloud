import sys
from datetime import *
from Authentication import *
from MongoDatabase import *
from GetInstanceStartTime import *

# from  import *


class GenerateBill:

	def __init__(self,cat,instName):

		inst = str(instName);
		cat = str(cat);
		print 'INST ->', inst;
		print 'CATG ->', cat;
		
		self.aObj = Authentication("yess");
		self.nova = self.aObj.getComputeClient();
		self.neutron = self.aObj.getNeutronClient();
		self.keystone= self.aObj.getKeystoneClient();
		self.glance = self.aObj.getGlanceClient();
		self.cclient = self.aObj.getCeilometerClient();

		self.dbObj = MongoDatabase();
		self.cat = cat;
		self.instName = inst;

	def getInstanceStartTime(self):

		obj1=GetInstanceStartTime()
		startTime = obj1.getEventTime('admin',self.instName)
		return startTime;

	def getInstanceTotalRunningTime(self):

		startTime = self.getInstanceStartTime();
		currTime = datetime.utcnow();

		print "STime  -->> ",startTime
		print "curr   -->> ",currTime

		hmsStrt = self.getTime(startTime);
		hmsCurr = self.getTime(currTime);
		
		hours=0;
		minutes=0;
		seconds=0;

		if(len(hmsStrt)==3 & len(hmsCurr)==3):

			hrs = int(hmsStrt[0]);
			mins = int(hmsStrt[1]);
			secs = int(hmsStrt[2]);
			start = timedelta(hours=hrs,minutes=mins,seconds=secs);

			hrs = int(hmsCurr[0]);
			mins = int(hmsCurr[1]);
			secs = int(hmsCurr[2]);
			end = timedelta(hours=hrs,minutes=mins, seconds=secs)

		return end - start;

	def getTime(self,currTime):

		currTime = str(currTime);

		if ('T' in currTime):
			currTime = currTime.replace("T", " ");

		dati = currTime.split(' ');
		timi = dati[1].split('.');
		hms = timi[0].split(":");

		return hms

	def getDBTime(self,currTime):

		currTime = str(currTime);
		if ('T' in currTime):
			currTime = currTime.replace("T", " ");
		dati = currTime.split(' ');
		timi = dati[1].split('.');
		return timi[0]

	def getDate(self,currDate):

		currDate = str(currDate);

		if ('T' in currDate):
			currDate = currDate.replace("T", " ");

		dati = currDate.split(' ');		
		return dati[0]

	def getFlavourName(self):

		ser = self.nova.servers.list();
		flv = self.nova.flavors.list();

		flvName="";
		for each in ser:
			if(each.name==(self.instName)):
			    for each2 in flv:
			        if (each2.id == each.flavor['id']):
			            flvName = each2.name
			else:
				return None;

		return flvName;

	def getTotalHours(self,ttime):

		ttime = str(ttime);
		hms = ttime.split(":");

		hrs = int(hms[0]);
		mins = int(hms[1]);
		secs = int(hms[2]);

		if(secs>0):
			mins=mins+1;

		if(mins>=5):
			hrs=hrs+1;

		return int(hrs);

	def getCurrentDate(self):

		currTime = datetime.utcnow();
		currTime = str(currTime);
	
		oi = currTime.split(' ');
		for i in range(0,len(oi)):
			return oi[i];

	def getCurrentTime(self):

		currTime = datetime.utcnow();
		currTime = str(currTime);

		oi = currTime.split(' ');
		timi = oi[1].split('.');
		return timi[0];


	def generateBillPlease(self):

		flvrName = self.getFlavourName();
		print 'Flvr : -->',flvrName

		ttime = self.getInstanceTotalRunningTime();
		print 'inst Time ->  ',ttime;
		
		hrs = self.getTotalHours(ttime);
		price = self.dbObj.getCategoryPriceChart(self.cat,flvrName);

		return self.makeDictionary(hrs,price);

	def getCategoryPrice(self):

		flvrName = self.getFlavourName();
		price = self.dbObj.getCategoryPriceChart(self.cat,flvrName);
		return price;

	def getTaxAmount(self,price):

		price = int(price);
		return (price*10)/100;

	def getTotal(self,amount,tax):

		amount = int(amount);
		tax = int(tax);
		return amount+tax;

	def makeDictionary(self,hrs,price):

		price = int(price);
		money = price*hrs;
		print 'Hrs -> ' , hrs
		print 'Price -> ' , price
		print 'Total Money -> ' , money

		instncID = self.getInstanceID(self.instName);

		query={};
		query['instance_id'] = instncID;
		query['consumed_hour'] = hrs;
		query['category'] = self.cat;
		query['amount'] = money;

		currTime = datetime.utcnow();
		print "Time --> ", currTime
		
		query['timestamp'] = currTime

		print '** Query Created **'
		print(query);
		self.saveToDatabasePlease(query);

		return query

	def saveToDatabasePlease(self,dbDict):

		dbObj = MongoDatabase();
		dbObj.addPaidBillToDatabase(dbDict);

	def getInstanceID(self,nami):

		ser = self.nova.servers.list();		
		for each in ser:
			if (each.name == nami):
				return each.id;
		return None;


# obj = GenerateBill('billi','bazuka');
# obj.generateBillPlease();