
# coding: utf-8

# In[ ]:




# In[5]:

#!/usr/bin/env python
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

class Events:
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


    def getEventsList(self):
        projectId=0
        query={}
        eventObj=[]
        eventDict = OrderedDict([])
        eventList=[]
        tenantList=[]
        trait=''
        tenantList=self.getTenantList()
        for each in tenantList:
            print each.name
            projectId=each.id
            query = [dict(field='project_id', op='eq', value=projectId)]
            eventObj=cclient.events.list(q=query,limit=4000)
            for each1 in eventObj:
#                 for i in each1.traits

#                      print "name:{},value:{}\n".format(i['name'],i['value'])

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
        return eventList


obj1=Events()
tempList=obj1.getEventsList()



#         for each2 in each1.traits:
#             print "name:{},value:{}\n".format(each2['name'],each2['value'])
#         print "\n"



# temp=0
# for each in eventObj:
# #      print "event_type:{}\ngeneratedAt:{}\nproject id:{}\n".format(each.event_type,each.generated,each.traits)
#     print each.project_id
#     print each.event_type
#     temp=len(each['traits'])
#     for i in range(temp):
#         if(each['traits'][i]['name']=='project_id'):
#             print 'l'

#     print "\n"

# print eventObj
# for i in tenantList:
#     print i
#     print "\n"
# for eventObj1 in eventObj:
#     traits=eventObj1.traits;
#     print "event_type:{}\ngeneratedAt:{}\nproject id:{}".format(eventObj1.event_type,eventObj1.generated,eventObj1.human_id)
#     print"\n"
#     print "traitsLen:",len(traits)
#     for i in range(0,len(traits),1):
#         print "{}:{}".format(traits[i]['name'],traits[i]['value'])
#     print "\n"
#     print eventObj1

# print "no of events:{}".format(len(eventObj))

# query = [dict(field='resource_id', op='eq', value=myInstanceId)]
# #eventObj = cclient.samples.list();

# #eventObj = cclient.meters.list();
# #eventObj = cclient.samples.list(q=query);
# eventObj = cclient.samples.list(meter_name="cpu",q=None);
# for each in eventObj:
#     print each.resource_metadata['display_name']
#     print "\n"
# print len(eventObj);

# print "#-----------------------------------------------------------------------#"
# or each in instances:
#     if(each.name == "demo-instance1" ):
#         myInstanceId = each.id;

# print myInstanceId;

# query = [dict(field='resource_id', op='eq', value=myInstanceId)]
# #eventObj = cclient.samples.list();

# #eventObj = cclient.meters.list();
# #eventObj = cclient.samples.list(q=query);
# eventObj = cclient.samples.list(meter_name="cpu",q=query);
# for each in eventObj:
#     print each
# print len(eventObj);




# query = [dict(field='resource_id', op='eq', value=myInstanceId)]

# kwargs = {"resource_id": myInstanceId, "counter_type": "gauge", "counter_name": "memory.usage", "counter_unit": "MB", "counter_volume": "48"}

# eventObj = cclient.samples.create(**kwargs)
#eventObj = cclient.samples.create(resource_id=myInstanceId,meter_type="gauge",meter_name="memory.usage",meter_unit="MB",sample_volume=48)


# for each in eventObj:
#     if(each.name=="cpu"):
#         print each.name + '--' + each.type;
#eventObj = cclient.new_samples.list(q=query, limit=10);
#eventObj = cclient.statistics.list('cpu_util',q=query, period=3600, groupby=None, aggregates=None);
#eventObj  = cclient.events.list();
#p = dir(eventObj);
#print p;
#xc = getattr(eventObj);
#print xc
#print repr(eventObj)
# eventObj=cclient


# In[ ]: