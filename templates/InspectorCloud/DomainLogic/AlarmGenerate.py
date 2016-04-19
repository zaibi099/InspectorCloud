#!/usr/bin/env python
import sys
from Authentication import *


class AlarmGenerate:

	def __init__(self,arguments):

		self.aObj = Authentication("yess");
		self.nova = self.aObj.getComputeClient();
		self.neutron = self.aObj.getNeutronClient();
		self.keystone= self.aObj.getKeystoneClient();
		self.glance = self.aObj.getGlanceClient();
		self.cclient = self.aObj.getCeilometerClient();
		self.args=arguments;

		for each in arguments:
			print "--->",each

	def createThreshAlarm(self):

		try:
			rscr=self.args[1];
			# print rscr
			namex=self.args[2];
			descrp=self.args[3];
			mtr_name=self.args[4];
			threshi=self.args[5];
			compar_op=self.args[6];
			stats=self.args[7];
			prd=self.args[8];
			evalPrd=self.args[9]
			insufficDataAction = self.args[10]
			okAction=self.args[11]
			# alarmAction=self.args[12]
			instId = self.getInstanceId(self.getInstanceName());
			print instId;

			threshi = int(threshi)
			prd = int(prd)
			evalPrd = int(evalPrd)

			threshAlarm = {"query": "[dict(field='resource_id',op='eq',value=instId),dict(field='alarm_actions',op='eq',value='log://'),dict(field='ok_actions',op='eq',value='log://'),dict(field='insufficient_data_actions',op='eq',value='log://')]",
						   "name":namex,
						   "description": descrp,
						   "meter_name": mtr_name, "threshold": threshi, "comparison_operator": compar_op,
						   "statistic":stats,"period":prd,"evaluation_periods":evalPrd}

			self.cclient.alarms.create(**threshAlarm);
		
		except:
			print '.'

	def getInstanceName(self):
		print self.args[1]
		return self.args[1]

	def getInstanceId(self,instanceName):

		instId=0;
		obj = self.nova.servers.list();

		for each in obj:
			if each.name==instanceName:
				instId=each.id;
				break;

		return instId;

#================== ALARM =============================

#state="no";    
#while(state!="alarm"):
#    state= cclient.alarms.get_state(each.id);
#    print state;
#    time.sleep(5);

#print "Alarm Bajj gya hi oyeeee\n\n\n";
# os.system("vlc ~/alarm.mp3");
