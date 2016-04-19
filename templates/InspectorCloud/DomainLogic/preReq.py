#!/usr/bin/env python
from os import environ as env
import os
import time
import glanceclient.v2.client as glclient

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

obj= nova.flavors.list();

flvrs=[];	 
for each in obj:
	flvrs.append(each.name);

obj= nova.images.list();	
imgz=[];	 
for each in obj:
	imgz.append(each.name);

obj= nova.networks.list();	
netwrk=[];	 
for each in obj:
	netwrk.append(each.label);

obj=nova.keypairs.list();	
keyz=[];	 
for each in obj:
	keyz.append(each.name);

print (keyz)

obj=nova.security_groups.list();
scrty=[];	 
for each in obj:
	scrty.append(each.name);
