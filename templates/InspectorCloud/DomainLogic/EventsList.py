
#!/usr/bin/env python
from os import environ as env
import os
from collections import OrderedDict
from pprint import pprint
from subprocess import Popen, PIPE
from Authentication import *
# from subprocess import Popen,PIPE
import subprocess
import re
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
    
    def getParsed(self,str2):
        str1=[]
        for u in str2.split(';'):

            str1.append(u.rstrip())

        return str1

    def getEventsList(self):
        name='admin'
        projectId=0
        query={}
        eventObj=[]
        eventDict = OrderedDict([])
        eventList=[]
        tenantList=[]
        trait=''
        listi=[]
        tName=evName=time=traits=""
        filename="events.txt"
        tenantList=self.getTenantList()
        for each in tenantList:
            if(name==each.name):

                stri=['./events',name,name,filename]


                process = Popen(stri, stdout=PIPE, stderr=PIPE)
                stdout, stderr = process.communicate()
                # print stderr
                # print stdout
                import os

                # print os.path.abspath("mydir/myfile.txt")

                # os.system('cd ~/fyp/PycharmProjects/MyProjects/InspectorCloud/DomainLogic')
                # print os.system('pwd')
                try:
                    import os.path
                    SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
                    CONFIG_PATH = os.path.join(SITE_ROOT, filename)
                    # print CONFIG_PATH
                    #
                    # print SITE_ROOT
                    out=open(CONFIG_PATH,'r')
                    str1=out.readline()

                    str2=self.getParsed(str1)


                    size=len(str2)
                    for i in range(0,size):
                        if i==0:

                            tName=str2[i]
                        elif i==1:

                            evName=str2[i]
                        elif i==2:
                            time=str2[i]
                        else:
                            traits=str2[i]

                    eventDict=([('tenantName',tName),
                    ('eventName',evName),
                    ('Generation Time',time),
                    ('traits',traits)])

                    eventList.append(eventDict)
                    while(str1!=""):

                        str1=out.readline()
                        # print str1
                        str2=self.getParsed(str1)
                        size=len(str2)

                        for i in range(0,size):

                            if i==0:
                                tName=str2[i]
                            elif i==1:

                                evName=str2[i]
                            elif i==2:
                                time=str2[i]
                            else:
                                traits=str2[i]

                        eventDict=([('tenantName',tName),
                        ('eventName',evName),
                        ('Generation Time',time),
                        ('traits',traits)])

                        eventList.append(eventDict)


                    out.close()
                except:
                    print "error"

        return eventList



# <codecell>

