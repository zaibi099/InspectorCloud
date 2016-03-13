from os import environ as env
import glanceclient.v2.client as glclient
import os
import time

import novaclient.client as kpk
from Authentication import *


from os import environ as env
import glanceclient.v2.client as glclient
import os
import time

import novaclient.client as kpk
from Authentication import *


authObj1=Authentication("zaib")
nova = authObj1.getComputeClient()


neutron = authObj1.getNeutronClient()


keystone = authObj1.getKeystoneClient()



cclient = authObj1.getCeilometerClient()

glance = authObj1.getGlanceClient()


class RunningInstances:
    def __init__(self,msg):
        print msg
    def getRunningInstanceList(self):
        dic_resources={}
        instanceList=nova.servers.list(search_opts={'all_tenants': 1})
        for i in range(0,len(instanceList),1):
            values = [instanceList[i].id,instanceList[i].name,instanceList[i].image['id'],instanceList[i].status]
            # values=[]
            dic_resources[instanceList[i].id]=values
        return dic_resources





# b=nova.quotas.defaults('3e08974a54234432ad580023eeb12c1b')
# print b
# a=nova.quotas.get('3e08974a54234432ad580023eeb12c1b',user_id='567c6acdf3514df9852a7142959e65d9')
#
# obj = nova.servers.list();
# memory=0;
#
# memory=0;
#
# for each in obj:
#     print each.id;
#     query = [dict(field='resource_id', op='eq', value=each.id)]
#     mx = cclient.samples.list(meter_name="memory.resident",q=query);
#     for each in mx:
#         memory = memory + each.counter_volume;
#         break;
#
# for each in obj:
#     print each.id;
#     query = [dict(field='resource_id', op='eq', value=each.id)]
#     mx = cclient.samples.list(meter_name="vcpu",limit=None);
#     for each in mx:
#         memory = each.counter_volume;
#         break;
#
# print memory;
