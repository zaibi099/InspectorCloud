# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from os import environ as env
import glanceclient.v2.client as glclient
import os
from pprint import pprint

def dump(alarmList):
    for attr in dir(alarmList):
        print "eventObj.%s = %s" % (attr, getattr(alarmList, attr))

import novaclient.client as kpk
nova = kpk.Client("2", auth_url=env['OS_AUTH_URL'],
                  username=env['OS_USERNAME'],
                  api_key=env['OS_PASSWORD'],
                  project_id=env['OS_TENANT_NAME'],
                  region_name=env['OS_REGION_NAME'])


import neutronclient.v2_0.client as neutronclient
neutron = neutronclient.Client(auth_url=env['OS_AUTH_URL'],
                               username=env['OS_USERNAME'],
                               password=env['OS_PASSWORD'],
                               tenant_name=env['OS_TENANT_NAME'],
                               region_name=env['OS_REGION_NAME'])

import keystoneclient.v2_0.client as ksclient
keystone = ksclient.Client(auth_url=env['OS_AUTH_URL'],
                           username=env['OS_USERNAME'],
                           password=env['OS_PASSWORD'],
                           tenant_name=env['OS_TENANT_NAME'],
                           region_name=env['OS_REGION_NAME'])


import ceilometerclient.client as cl
cclient = cl.get_client( '2',
                         username=env['OS_USERNAME'],
                         password=env['OS_PASSWORD'],
                         tenant_name=env['OS_TENANT_NAME'],
                         auth_url=env['OS_AUTH_URL'])

glance_endpoint = keystone.service_catalog.url_for(service_type='image')
glance = glclient.Client(glance_endpoint, token=keystone.auth_token)
#     AdminList=[]
#     DemoList=[]
#     NoList=[]
#     myList0=cclient.meters.list()
#     for i in myList0:
#         print i
#         print "\n"
#     print"======================================================================"
#     adminInstanceId='026ffb61-df49-4e94-a06d-419b0bf0d329'
#     demoInstanceId='5f46a2db-7aff-4796-bca1-9a3dc46d69f1'
#     query = [dict(field='resource_id', op='eq', value=adminId)]
#     myList1=cclient.meters.list(q=query,limit=None)
#     for temp1 in myList1:

#         print "Name:{} Unit:{} Type:{} Tenant id:{} Instance Name:{}".format(temp1.name,temp1.unit,temp1.type,temp1.project_id,"Admin Instance")
#         print "\n"
#     print len(myList1)
#     print"======================================================================"
#     query = [dict(field='resource_id', op='eq', value=demoId)]
#     myList2=cclient.meters.list(q=query,limit=None)
#     for temp1 in myList2:

#         print "Name:{} Unit:{} Type:{} Tenant id:{} Instance Name:{}".format(temp1.name,temp1.unit,temp1.type,temp1.project_id,"Demo Instance")
#         print "\n"
#     print len(myList2)


#     print"======================================================================"
#     from  more_itertools import unique_everseen
tenantList=keystone.tenants.list(limit=None,marker=None)
metersDict={}
list1=[]
query=[]
for each1 in tenantList:
    print each1.id
    print each1.name
    print "\n"
    query = [dict(field='project_id', op='eq', value=each1.id)]
    list1=cclient.meters.list(q=query,limit=2000)
    metersDict.update({each1.name:list1 })

for each in metersDict:
    print each
    list1=metersDict[each]
    for i in list1:
        print "Name:{} Unit:{} Type:{} Tenant Name:{}".format(i.name,i.unit,i.type,each)
        print "\n"
    print "length:{}".format(len(list1))
    print"======================================================================"
#     myList6=list(unique_everseen(myList3))
#     myList4=list(set(myList3)-set(myList2))
#     myList5=list(set(myList4)-set(myList1))
#     for temp1 in myList3:

#         print "Name:{} Unit:{} Type:{} Tenant id:{} Instance Name:{}".format(temp1.name,temp1.unit,temp1.type,temp1.project_id,"Admin Instance")
#         print "\n"
#     print len(myList3)

#     print"======================================================================"
#     query = [dict(field='project_id', op='eq', value=demoTenantId)]
#     myList4=cclient.meters.list(q=query,limit=None)
#     for temp1 in myList4:

#         print "Name:{} Unit:{} Type:{} Tenant id:{} Instance Name:{}".format(temp1.name,temp1.unit,temp1.type,temp1.project_id,"Demo Instance")
#         print "\n"
#     print len(myList4)
#     print"======================================================================"
#     query = [dict(field='project_id', op='eq', value='')]
#     myList4=cclient.meters.list(q=None,limit=200)
#     for temp1 in myList4:

#         print "Name:{} Unit:{} Type:{} Tenant id:{} Instance Name:{}".format(temp1.name,temp1.unit,temp1.type,temp1.project_id,"Demo Instance")
#         print "\n"
#     print len(myList4)
#     print"======================================================================"
#     myList5=[]
#     for temp1 in myList4:
#         if temp1.project_id==adminTenantId or temp1.project_id==demoTenantId:
#             myList5.append(temp1)

#     myList6=list(set(myList4)-set(myList5))
#     for temp1 in myList6:

#         print "Name:{} Unit:{} Type:{} Tenant id:{} Instance Name:{}".format(temp1.name,temp1.unit,temp1.type,temp1.project_id,"Demo Instance")
#         print "\n"
#     print len(myList6)

#     query = [dict(field='resource_id', op='eq', value=demoTenantId)]
#     myList4=cclient.meters.list(q=None,limit=None)
#     for temp1 in myList4:

#         print "Name:{} Unit:{} Type:{} Tenant id:{} Instance Name:{}".format(temp1.name,temp1.unit,temp1.type,temp1.project_id,"Demo Instance")
#         print "\n"
#     print len(myList4)

#     for temp1 in myList1:
#         if temp1.resource_id.find('026ffb61-df49-4e94-a06d-419b0bf0d329')!=-1:
#             AdminList.append(temp1)
#             #print "Name:{} Unit:{} Type:{} Tenant id:{} Instance Name:{}".format(temp1.name,temp1.unit,temp1.type,temp1.project_id,"Admin Instance")
#         elif temp1.resource_id.find('5f46a2db-7aff-4796-bca1-9a3dc46d69f1')!=-1:
#             DemoList.append(temp1)
#             #print "Name:{} Unit:{} Type:{} Tenant id:{} Instance Name:{}".format(temp1.name,temp1.unit,temp1.type,temp1.project_id,"Demo Instance")
#         else:
#             NoList.append(temp1)
#             #print "Name:{} Unit:{} Type:{} Tenant id:{} Instance Name:{}".format(temp1.name,temp1.unit,temp1.type,temp1.project_id,"No instance")


#     for i in AdminList:
#         print "Name:{} Unit:{} Type:{} Tenant id:{} Resource id:{} Instance Name:{}".format(i.name,i.unit,i.type,i.project_id,i.resource_id,"Admin Instance")
#     print"======================================================================"
#     for i in DemoList:
#         print "Name:{} Unit:{} Type:{} Tenant id:{} Resource id:{} Instance Name:{}".format(i.name,i.unit,i.type,i.project_id,i.resource_id,"Demo Instance")
#     print"======================================================================"
#     for i in NoList:
#         print "Name:{} Unit:{} Type:{} Tenant id:{} Resource id:{} Instance Name:{}".format(i.name,i.unit,i.type,i.project_id,i.resource_id,"No Instance")
#     print"======================================================================"
#     myList2=cclient.resources.list()
#     for j in myList2:
#         print j
#         print "\n"


