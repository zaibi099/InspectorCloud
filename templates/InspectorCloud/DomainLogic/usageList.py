from os import environ as env
import glanceclient.v2.client as glclient
import os
import time

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


instanceList=nova.servers.list(search_opts={'all_tenants': 1})
dic_resources=[]
for i in range(0,len(instanceList),1):
    values = [instanceList[i].id,instanceList[i].name,instanceList[i].image['id'],instanceList[i].status]
    # values=[]
    dic_resources.append(values)
# print dic_resources








b=nova.quotas.defaults('3e08974a54234432ad580023eeb12c1b')
# print b
a=nova.quotas.get('3e08974a54234432ad580023eeb12c1b',user_id='567c6acdf3514df9852a7142959e65d9')

obj = nova.servers.list();
memory=0;

memory=0;

for each in obj:
    # print each.id;
    query = [dict(field='resource_id', op='eq', value=each.id)]
    mx = cclient.samples.list(meter_name="memory.resident",q=query);
    for each in mx:
        memory = memory + each.counter_volume;
        break;
        
for each in obj:
    # print each.id;
    query = [dict(field='resource_id', op='eq', value=each.id)]
    mx = cclient.samples.list(meter_name="vcpu",limit=None);
    for each in mx:
        memory = each.counter_volume;
        break;

# print memory;
