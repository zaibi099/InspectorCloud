from os import environ as env
import os
import re
from datetime import datetime, timedelta
from pprint import pprint
from collections import OrderedDict
from Authentication import *


authObj1=Authentication("zaib")
nova = authObj1.getComputeClient()


neutron = authObj1.getNeutronClient()


keystone = authObj1.getKeystoneClient()



cclient = authObj1.getCeilometerClient()

glance = authObj1.getGlanceClient()

class ResourcesQuotas:

    def __init__(self,str):
        temp=0
        self.mfIp=0
        self.tfIp=0
        self.mIn=0
        self.tIn=0
        self.mCo=0
        self.tCo=0
        self.mRam=0
        self.tRam=0
        self.tKeyP=0
        self.mKeyP=0
        self.mSG=0
        self.tSG=0
        self.TName=""
        print str
    def getTenantId(self,name):
        tenantList=keystone.tenants.list(limit=None,marker=None)
        id=0
        for each in tenantList:
            if each.name==name:
                id=each.id
        return id
    def getTenantsNames(self):
        nameList=[]
        tenantList=keystone.tenants.list(limit=None,marker=None)

        for each in tenantList:
            nameList.append(each.name)
        return nameList
    def getAllResources(self,name):
        tId=self.getTenantId(name)

        limits=nova.limits.get(tenant_id=tId)

        for each in limits.absolute:
            if each.name=='maxTotalInstances':
                self.mIn=each.value
            elif  each.name=='totalInstancesUsed':
                self.tIn=each.value
            elif each.name=='maxTotalRAMSize':
                self.mRam=each.value
            elif  each.name=='totalRAMUsed':
                self.tRam=each.value
            elif each.name=='maxTotalKeypairs':
                self.mKeyP=each.value
            elif each.name=='totalSecurityGroupsUsed':
                self.tSG=each.value
            elif each.name=='maxSecurityGroups':
                self.mSG=each.value
            elif each.name=='maxTotalCores':
                self.mCo=each.value
            elif each.name=='totalCoresUsed':
                self.tCo=each.value
            else:
                print ""
        keyPairs=self.getKeyPairsForOtherTenants(name)
        self.TName=name

        self.tKeyP =  keyPairs
        floatingIps=self.getMaxFloatingIp(tId)
        self.mfIp =  floatingIps[0]
        self.tfIp= floatingIps[1]

    def getMaxFloatingIp(self,inputi):
        i=0
        var=neutron.show_quota(tenant_id=inputi,profile=None)
        temp=neutron.list_floatingips(profile=None)
        for each in temp['floatingips']:
            if each['tenant_id']==inputi:
                i=i+1


        return [var['quota']['floatingip'],i]
    def getKeyPairsForOtherTenants(self,inputVar):
        from subprocess import Popen,PIPE
        tenant=inputVar
        stri ="./kk "+tenant+" "+tenant

        p = Popen(stri,stdout=PIPE, shell=True,stdin=PIPE).stdout;
        k = p.readlines();


        var=0;
        lt = len(k)-1;
        num=0;

        for each in k:
            if((var>=4) & (var != lt)):
                num=num+1;
            var=var+1;


        return num







