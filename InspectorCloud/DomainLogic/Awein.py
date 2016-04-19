#!/usr/bin/env python
import sys
from os import environ as env
import neutronclient.v2_0.client as neutronclient
import novaclient.client as kpk
import glanceclient.v2.client as glclient
import keystoneclient.v2_0.client as ksclient
import ceilometerclient.client as cl
import os

nova = kpk.Client("2", auth_url=env['OS_AUTH_URL'],
                  username=env['OS_USERNAME'],
                  api_key=env['OS_PASSWORD'],
                  project_id=env['OS_TENANT_NAME'],
                  region_name=env['OS_REGION_NAME'])

neutron = neutronclient.Client(auth_url=env['OS_AUTH_URL'],
                               username=env['OS_USERNAME'],
                               password=env['OS_PASSWORD'],
                               tenant_name=env['OS_TENANT_NAME'],
                               region_name=env['OS_REGION_NAME'])

keystone = ksclient.Client(auth_url=env['OS_AUTH_URL'],
                           username=env['OS_USERNAME'],
                           password=env['OS_PASSWORD'],
                           tenant_name=env['OS_TENANT_NAME'],
                           region_name=env['OS_REGION_NAME'])

keystone = self.getKeystoneClient();
glance_endpoint = keystone.service_catalog.url_for(service_type='image')
glance = glclient.Client(glance_endpoint, token=keystone.auth_token)

cclient = cl.get_client( '2',
                         username=env['OS_USERNAME'],
                         password=env['OS_PASSWORD'],
                         tenant_name=env['OS_TENANT_NAME'],
                         auth_url=env['OS_AUTH_URL'])

bodyVal= {
    "alarm_actions": ['alarmAction'],
    "alarm_id": '12312',
    "combination_rule": 'null',
    "description": 'descrp',
    "enabled": 'true',
    "insufficient_data_actions": ['insufficDataAction'],
    "name": "NewAlarm",
    "ok_actions": ['okAction'],
    #                     "project_id": "c96c887c216949acbdfbd8b494863567",
    "repeat_actions": 'false',
    "state": "OK",
    #                 "state_timestamp": "2013-11-21T12:33:08.486228",
    #                 "threshold_rule": nill,
    #                 "timestamp": "2013-11-21T12:33:08.486221",
    "type": "threshold",
    #                 "user_id": "c96c887c216949acbdfbd8b494863567"
    "instance_id" : 'instId'
}

# 		threshAlarm = {"query": "[dict(field='resource_id',op='eq',value=instId),dict(field='alarm_actions',op='eq',value=alarmAction),dict(field='ok_actions',op='eq',value=okAction),dict(field='insufficient_data_actions',op='eq',value=insufficDataAction)]",
# 					   "name":namex,
# 					   "description": descrp,
# 					   "meter_name": mtr_name, "threshold": threshi, "comparison_operator": compar_op,
# 					   "statistic":stats,"period":prd,"evaluation_periods":evalPrd}

# 		self.cclient.alarms.create(**threshAlarm);

cclient.alarms.create(data=bodyVal);


args=[];
args.append("nammmeee");
args.append("bazuka");
args.append("maLarm");
args.append("Descrp");
args.append("disk.read.requests");
args.append("1");
args.append("gt");
args.append("count");
args.append("60");
args.append("3");
args.append("log://");
args.append("log://");
args.append("log://");
alarmObj = AlarmGenerate(args);
alarmObj.createThreshAlarm();
#================== ALARM =============================

#state="no";
#while(state!="alarm"):
#    state= cclient.alarms.get_state(each.id);
#    print state;
#    time.sleep(5);

#print "Alarm Bajj gya hi oyeeee\n\n\n";
# os.system("vlc ~/alarm.mp3");
