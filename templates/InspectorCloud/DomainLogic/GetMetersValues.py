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

class GetMetersValues:
    
    def _init_(self):
        temp=0
    
    def getInstanceDict(self):
        myDict={}

        instanceList=nova.servers.list(search_opts={'all_tenants': 1})
        for each in instanceList:
            myDict[each.id]=each.name
        return myDict
    
    def getInstanceId(self,i):
        
        instanceList=nova.servers.list(search_opts={'all_tenants': 1})
        instanceId=0
        for each in instanceList:
            if(each.name==i):
                instanceId=each.id
        return instanceId
    
    
    def getInstanceName(self,i):
       
        instanceDict={}
        instanceName=''
        instanceDict=self.getInstanceDict()
        temp1=''
        for each in instanceDict:
            temp1=each
            if(temp1 in i.resource_id ):
                instanceName=instanceDict[each]
                break
        # if(instanceName==''):
        #     instanceName='Not instance Related'
        return instanceName
    
    
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
    
    
    def getTenantList(self):
        tenantList=keystone.tenants.list(limit=None,marker=None)
        return tenantList
    
    
    def getMetersForAllTenants(self):
        metersDict={}
        tenantList=[]
        tenantList=self.getTenantList()
        for each1 in tenantList:
            query0 = [dict(field='project_id', op='eq', value=each1.id)]
            list1=cclient.meters.list(q=query0,limit=2000)
            metersDict.update({each1.name:list1 })
        return metersDict
   
    
    def getSamplesStat(self):
        
        metersDict={}
        list1=[]
        temp0=temp1=[]
        minVar=maxVar=avgVar=sumVar=0.0
        query0=query1=query2=[]
        endDateUtcVar = datetime.utcnow()
        startDateUtcVar = endDateUtcVar-timedelta(hours=1)
        tenantName=''
        serviceName=''
        instanceNam=''
        sampleDict = OrderedDict([])
        sampleList=[]
        
        metersDict=self.getMetersForAllTenants()
#         print metersDict
        for each  in metersDict:

            tenantName= each
            
        #     print each
            for i in metersDict[each]:
                serviceName=self.getServiceName(i.name)
                instanceName=self.getInstanceName(i)
                if(instanceName==''):
                    instanceName='project-related'

                if (
                    i.name=='cpu.delta' or i.name=='cpu' or i.name=='storage.objects.size' or
                    i.name=='storage.containers.objects.size' or i.name=='image.size' or i.name=='disk.allocation' or
                    i.name=='disk.capacity' or i.name=='disk.usage' or i.name=='disk.read.bytes' or
                    i.name=='disk.device.capacity' or i.name=='disk.device.read.bytes' or i.name=='disk.device.usage' or
                    i.name=='disk.device.allocation'
                    ):



        #             print ("Date and time in ISO format = %s" % dateVar.isoformat() )
                    query1=[dict(field='project_id', op='eq', value=i.project_id),dict(field='instance_id',op='eq',value='dd78106e-2828-4af8-9c05-171b36b5c5a8'),dict(field='timestamp',op='ge',value=startDateUtcVar.isoformat()),dict(field='timestamp',op='le',value=endDateUtcVar.isoformat())]
                
                    temp0=cclient.samples.list(meter_name=i.name,q=query1,limit=4000)

                    minVar=maxVar=avgVar=sumVar=0.0

                    for j in range(len(temp0)):
                        if j==0:
                            minVar=temp0[j].counter_volume
                            maxVar=temp0[j].counter_volume
                            sumVar+=temp0[j].counter_volume
                        else:

                            sumVar+=temp0[j].counter_volume

                            if temp0[j].counter_volume<minVar:
                                minVar=temp0[j].counter_volume

                            if temp0[j].counter_volume>maxVar:
                                maxVar=temp0[j].counter_volume
                    if len(temp0)>0:
                        avgVar=sumVar/len(temp0)
                    else:
                        avgVar=0.0

        #             print "Tenant Name:{},Service:{},Meter Name:{},Min:{},Max:{},Avg:{},Type:{},Unit:{}\n".format(tenantName,serviceName,i.name,minVar,maxVar,avgVar,i.type,i.unit)
                    sampleDict=([('tenantName',tenantName),
                                 ('instanceName',instanceName),
                             ('service',serviceName),
                             ('meter',i.name),
                             ('min',minVar),
                             ('max',maxVar),
                             ('avg',avgVar),
                             ('meterType',i.type),
                             ('meterUnit',i.unit)
                             ])
                    sampleList.append(sampleDict)


                else:
                    query2=[dict(field='project_id',op='eq',value=i.project_id),dict(field='timestamp',op='ge',value=startDateUtcVar.isoformat()),dict(field='timestamp',op='le',value=endDateUtcVar.isoformat())]
                    temp1=cclient.statistics.list(meter_name=i.name,q=query2)

        #
                    for each in temp1:
        #                 print "Tenant Name:{},Service:{},Meter Name:{},Min:{},Max:{},Avg:{},Type:{},Unit:{}\n".format(tenantName,serviceName,i.name,each.min,each.max,each.avg,i.type,i.unit)
                        minVar=each.min
                        maxVar=each.max
                        avgVar=each.avg
                        sampleDict=([('tenantName',tenantName),
                                     ('instanceName',instanceName),
                                 ('service',serviceName),
                                 ('meter',i.name),
                                 ('min',minVar),
                                 ('max',maxVar),
                                 ('avg',avgVar),
                                 ('meterType',i.type),
                                 ('meterUnit',i.unit)
                                 ])
                        sampleList.append(sampleDict)
                        
        return sampleList
    
    
    def getSampleVal(self,mName,iName,tName):
        
        iId=self.getInstanceId(iName)
        print iId
        tId=0
        projects=self.getTenantList()
        for each in projects:
            if(each.name==tName):
                tId=each.id
        
        endDateUtcVar = datetime.utcnow()
        startDateUtcVar = endDateUtcVar-timedelta(hours=1)
        query1=[dict(field='project_id', op='eq', value=tId),dict(field='resource_id',op='eq',value=iId),dict(field='timestamp',op='ge',value=startDateUtcVar.isoformat()),dict(field='timestamp',op='le',value=endDateUtcVar.isoformat())]
        temp0=cclient.samples.list(meter_name=mName,q=query1,limit=4000)
        return temp0