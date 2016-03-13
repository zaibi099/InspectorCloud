#!/usr/bin/env python
from os import environ as env
import glanceclient.v2.client as glclient
import os
import time
import sys
import subprocess
	
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

obj = cclient.alarms.list();

obj = cclient.alarms.list();
count=len(obj);

for i in range(0,count,1):
	if(obj[i].state=="alarm"):
		try:
			stri = "cvlc --vout none alarm.mp3";
			subprocess.Popen(stri,stdout=subprocess.PIPE, shell=True)
		except:
			print("---");
	else:
		
         print("na ker")



    #================== ALARM =============================

    #state="no";
    #while(state!="alarm"):
    #    state= cclient.alarms.get_state(each.id);
    #    print state;
    #    time.sleep(5);

    #print "Alarm Bajj gya hi oyeeee\n\n\n";
    # os.system("vlc ~/alarm.mp3");
