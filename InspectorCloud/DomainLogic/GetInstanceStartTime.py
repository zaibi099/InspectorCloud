from os import environ as env
import os
from collections import OrderedDict
from pprint import pprint
from Authentication import *


authObj1=Authentication("zaib")
nova = authObj1.getComputeClient()
neutron = authObj1.getNeutronClient()
keystone = authObj1.getKeystoneClient()
cclient = authObj1.getCeilometerClient()
glance = authObj1.getGlanceClient()

class GetInstanceStartTime:

    def __init__(self):
        i=0
    
    def getInstanceName(self,temp):
    
        id=''
        traits=temp.traits
        for each2 in traits:
                if(each2['name']=='instance_id'):
                    id=each2['value']
                    break
        instanceList=nova.servers.list(search_opts={'all_tenants': 1},marker=None,limit=None)
        name=''
        for n in instanceList:
            if(n.id==id):
                name=n.name
                break
        return name
    

    def getImageName(self,each1):
        traits=each1.traits
        name=''
        for each2 in traits:
                if(each2['name']=='name'):
                    name=each2['value']
                    break
        return name
    

    def getTenantList(self):
    
        tenantList=keystone.tenants.list(limit=None,marker=None)
        return tenantList
    
    
    
    def getEventTime(self,projectName,iName):
    
        projectId=0
        query={}
        eventObj=[]
        eventDict = OrderedDict([])
        eventList=[]
        tenantList=[]
        trait=''

        tenantList=self.getTenantList()
        for each in tenantList:
            if each.name==projectName:
                projectId=each.id
                query = [dict(field='project_id', op='eq', value=projectId)]
                eventObj=cclient.events.list(q=query,limit=4000)
#                 for e in eventObj:
#                     print e
#                     print "\n"
            for each1 in eventObj:
                if('compute' in each1.event_type):
                    trait=self.getInstanceName(each1)
                elif('image' in each1.event_type):
                    trait=self.getImageName(each1)
                else:
                    trait='none'
                eventDict=([('tenantName',each.name),
                             ('eventName',each1.event_type),
                             ('Generation Time',each1.generated),
                             ('traits',trait)
                             ])
                eventList.append(eventDict)
        reqTime=""
        
        for each in eventList:
            
            dct = dict(each)
            if dct['eventName']=='compute.instance.create.end' and dct['traits']==iName:
                reqTime=dct['Generation Time']

        return reqTime

                
# obj1=Events()
# iName='bad'
# time=obj1.getEventTime('admin',iName)
# print time

        

