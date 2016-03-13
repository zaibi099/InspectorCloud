#!/usr/bin/env python
from os import environ as env
import glanceclient.v2.client as glclient
import os
import time
import sys


args=[None]*7;
itr=0;

for arg in sys.argv:
	print arg;
	args[itr]=arg;
	itr=itr+1;

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
                          

                         
glance_endpoint = keystone.service_catalog.url_for(service_type='image')
glance = glclient.Client(glance_endpoint, token=keystone.auth_token)


devLoc = "~/FYP/devstack";

securityGroup = args[4];
flvrName=args[1];
imageName=args[2];
instanceName=args[6];

keyName=args[5];

neti = nova.networks.list()
desiredNet = args[3];
netId=None;

if neti is None:
	print 'empty'
else:
	#print 'Something in Nets'
	for x in neti:
		if x.label == desiredNet:
			netId = x.id;
			break

#============================

stri= "nova boot --flavor {} --image {} --nic net-id={} --security-group {} --key-name {} {}".format(flvrName,imageName,netId,securityGroup,keyName,instanceName)
print(stri);        

os.system(stri);
time.sleep(7)
        
nova_ips = nova.floating_ip_pools.list();
floating_ip = nova.floating_ips.create(nova.floating_ip_pools.list()[0].name);
        
ser = nova.servers.list();
server=0;
        
for each in ser:
	if(each.name==instanceName):
		server = each;
		break;
        
nova.servers.add_floating_ip(server,floating_ip.ip);
group = nova.security_groups.find(name=securityGroup);
nova.security_group_rules.create(group.id, ip_protocol="tcp" ,from_port=22, to_port=22);
nova.security_group_rules.create(group.id, ip_protocol="icmp",from_port=-1, to_port=-1);

print "Ja bachiyeeaaa Ayashi Maarr...";

