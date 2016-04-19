#!/usr/bin/env python
import re
from Authentication import *
from GetMetersValues import *

class AlarmPreReq:

    def __init__(self):

        self.aObj = Authentication("yess");
        self.nova = self.aObj.getComputeClient();
        self.neutron = self.aObj.getNeutronClient();
        self.keystone= self.aObj.getKeystoneClient();
        self.glance = self.aObj.getGlanceClient();
        self.cclient = self.aObj.getCeilometerClient();

    def getServiceName(self,meterName):
        serviceName=''
        if(re.match(r'storage', meterName)):
            serviceName="swift"
        elif(re.match(r'image',meterName)):
            serviceName="glance"
        elif(re.match(r'volume',meterName)):
            serviceName="cinder"
        else:
            serviceName="nova"

        return serviceName

    def getAllMeters(self):

        tenantList=self.keystone.tenants.list(limit=None,marker=None)
        metersDict={}
        list1=[]
        meterList=[]
        name=''

        for each1 in tenantList:
            if(each1.name=='admin'):
                query0 = [dict(field='project_id', op='eq', value=each1.id)]
                list1=self.cclient.meters.list(q=query0,limit=2000)

        temp=[]
        novaMeters=[]
        for each in list1:
            name= self.getServiceName(each.name)
            if(name=='nova'):
                temp.append(each.name)

        novaMeters=list(set(temp))
        return novaMeters;

    def getInstances(self):
        obj= self.nova.servers.list();
        sers=[];

        for each in obj:
            sers.append(each.name);

        return sers;

    def getAllStats(self):

        statsi = ['count','max','sum','avg','min'];
        return statsi

    def getAllComparisonOperators(self):

        compOpr = ['gt','lt','ne','ge','le','eq']
        return compOpr;

    def getAllAlarmList(self):
        return self.cclient.alarms.list();

    def getAllMetersValues(self,alList):

        instanceList = self.nova.servers.list(search_opts={'all_tenants': 1});

        for i in range(0,len(alList)):
            print '>>--- aList --<<'
            instName = alList[i].description;
            mtr = alList[i].threshold_rule['meter_name'];
            val = self.getMeterValue(instName,mtr);            
            val = self.convertVal(val);         
            alList[i].severity = val;
            print '-->',val;

        return alList;

    def convertVal(self,val):

        val = str(val);

        if (val.find("['") != -1):
            
            val = val.replace("['","");
            val = val.replace("']","");
            return val;

        else:
            return val;

    def getInstanceID(self,instName):

        for i in range(0,len(instanceList),1):
            
            name = instanceList[i].name;
            if( name == instName ):
                return instanceList[i].id

    def getMeterValue(self,instName,mtr):

        obj1 = GetMetersValues();

        print "i : {} , mtr:  {}".format(instName,mtr);
        tenant ='admin';
        dic=obj1.getSampleVal(mtr,instName,tenant);

        li=[];
        print len(dic);

        for each in dic:
            stri=each.counter_name+","+each.resource_id+","+each.timestamp+","+str(each.counter_volume);
            print '----',each.counter_volume
            li.append(str(each.counter_volume));
            break;

        return li

# obj = AlarmPreReq();
# alList = obj.getAllAlarmList();
# aa = obj.getAllMetersValues(alList);

# for each in aa:
#     print each.name
#     print '-->',each.severity;