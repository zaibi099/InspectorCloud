#!/usr/bin/env python
import re
from Authentication import *

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
