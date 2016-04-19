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

class EventsHelper:
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


    def getEventsList(self,name):
        projectId=0
        query={}
        eventObj=[]
        eventDict = OrderedDict([])
        eventList=[]
        tenantList=[]
        trait=''
        tenantList=self.getTenantList()


        for each in tenantList:

            if(name==each.name):
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

	    else:
			i=0

        return eventList

    def saveEvents(self,name,dicto):
        # print os.system("pwd")
        # print os.system("/fyp/PycharmProjects/MyProjects/")
        import os.path
        SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
        CONFIG_PATH = os.path.join(SITE_ROOT, name)
        f = open(CONFIG_PATH,'w')
        # print os.path.abspath("mydir/myfile.txt")
        for each in dicto:
                # print each
            i=0
            for k,v in each:

                if i<3:
                    f.write(v+";")
                else:
                    f.write(v)
                i=i+1

            f.write("\n")

        f.close()
        return None




import sys

# Get the total number of args passed to the demo.py
total = len(sys.argv)

# Get the arguments list
cmdargs = str(sys.argv)


obj1=EventsHelper()
tempList=obj1.getEventsList(sys.argv[1])
# print tempList

# print tempList

filename=sys.argv[2]
obj1.saveEvents(filename,tempList)



