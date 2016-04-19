from pymongo import MongoClient

class MongoDatabase:

	def __init__(self):

		print 'object Created'
		self.client = MongoClient()
		# client = MongoClient('localhost', 27017)


	def addBillCategory(self,billData):

		if(self.databaseExists("mongoDB")==True):

			print 'True'
			db = self.client.mongoDB;
			coll = db['billCategory'];
			
			if(self.checkCategoryDuplicate(billData)==False):
				
				coll.insert_one(billData);
				print 'Row added'			
			
			else:
				print 'Duplicate Found'
		
		else:
			self.createDatabase();
			self.createBillCategoryDatabase(billData);

	def checkCategoryDuplicate(self,billData):

		db = self.client.mongoDB;
		coll = db['billCategory']; 
		
		ret = coll.find( {"name" : billData['name'] });

		if(ret.count()>0):
			return True
		else:
			return False

	def getAllBillCat(self):

		print "** GET ALL BILLS **"
		if(self.databaseExists("mongoDB")==True):
			
			db = self.client.mongoDB;
			coll = db['billCategory'];

			ret = coll.find();
			catNames=[];

			if(ret.count()>0):
				for each in ret:
					catNames.append(each['name']);
					print each['name']

				print len(catNames);
				return catNames
			
			else:
				return False

	def getCategoryPriceChart(self,catg,flvr):

		if( "." in flvr):
			flvr = flvr.replace(".","\\uff0e");
			print flvr

		if(self.databaseExists("mongoDB")==True):

			db = self.client.mongoDB;
			coll = db['billCategory'];

			print catg;

			ret = coll.find({"type" : "flvr_based","name":catg});
			dicti={};

			if(ret.count()==1):
				
				print ret.count()
				try:
					for each in ret:
						print each['priceList'][flvr]
						return each['priceList'][flvr];
				except:
					print 'Flavour Name is wrong'

		return None

	def databaseExists(self,db_name):

		db = self.client[str(db_name)];

		if bool(db_name in self.client.database_names()):
			return True;
		else:
			return False;

	def createDatabase(self):
		db = self.client['mongoDB'];
		return True;

	def createBillCategoryDatabase(self,billData):

		coll = db['billCategory'];
		coll.insert_one(billData);
		print 'Category Added'


	# =================== PAID BILLS ========================
	# =================== PAID BILLS ========================
	# =================== PAID BILLS ========================




	def createPaidBillDatabase(self,billData):

		coll = db['PaidBills'];
		coll.insert_one(billData);
		print 'Paid Bill Added'

	def addPaidBillToDatabase(self,billData):

		if(self.databaseExists("mongoDB")==True):

			print 'True'
			db = self.client.mongoDB;
			coll = db['paidBills'];
			coll.insert_one(billData);
			print 'Row added'
		
		else:
			self.createPaidBillDatabase(billData);

	def getAllPaidBills(self):

		if(self.databaseExists("mongoDB")==True):

			db = self.client.mongoDB;
			coll = db['paidBills'];

			listi=[];
			
			cursor = coll.find();
			
			for document in cursor:
				
				billList = {};
				billList['category']=document['category'];
				billList['consumed_hour']=document['consumed_hour'];
				billList['instance_id']=document['instance_id'];
				billList['amount']=document['amount'];
				billList['timestamp']=document['timestamp'];
				listi.append(billList);

			return listi;
		else:
			print "No DB Exists"
			return None;
			
#     ******************************************************************
# 	  ******************************************************************


	# =================== USER DB ========================
	# =================== USER DB ========================
	# =================== USER DB ========================


	def createUserDatabase(self,billData):

		coll = db['users'];
		coll.insert_one(billData);
		print 'User Added'


	def addUserToDatabase(self,billData):

		if(self.databaseExists("mongoDB")==True):

			print 'True'
			db = self.client.mongoDB;
			coll = db['users'];
			coll.insert_one(billData);
			print 'Row added'
		
		else:
			self.createUserDatabase(billData);

	def verifyUserLogin(self,userName,password):

		if(self.databaseExists("mongoDB")==True):

			db = self.client.mongoDB;
			coll = db['users'];
			cursor = coll.find();
			
			for document in cursor:
				if(document['user_name']==userName):
					print 'YES USER FOUND'
					if(document['password']==password):
						print 'YES PASS MATCH'
						return True;

		else:
			print "No DB Exists"
			return False;



obj = MongoDatabase();

billData = {
"name":"Umar Usaf",
"user_name":"umar902",
"password":"123",
"location":"Islamabad,Punjab,Pakistan",
"Occupation":"student",
"phone":"03046434356",
"email":"umarusaf902@gmail.com",
"instances":[],
};

obj.addUserToDatabase(billData);