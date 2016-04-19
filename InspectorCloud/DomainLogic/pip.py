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

# obj = RunningInstances();
# obj.