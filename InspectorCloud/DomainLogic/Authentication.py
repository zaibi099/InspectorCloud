#!/usr/bin/env python
from os import environ as env
import neutronclient.v2_0.client as neutronclient
import novaclient.client as kpk
import glanceclient.v2.client as glclient
import keystoneclient.v2_0.client as ksclient
import ceilometerclient.client as cl
import os

class Authentication:

    def __init__(self,msg):
        print msg;

    def getComputeClient(self):

        nova = kpk.Client("2", auth_url=env['OS_AUTH_URL'],
                          username=env['OS_USERNAME'],
                          api_key=env['OS_PASSWORD'],
                          project_id=env['OS_TENANT_NAME'],
                          region_name=env['OS_REGION_NAME'])
        return nova

    def getNeutronClient(self):

        neutron = neutronclient.Client(auth_url=env['OS_AUTH_URL'],
                                   username=env['OS_USERNAME'],
                                   password=env['OS_PASSWORD'],
                                   tenant_name=env['OS_TENANT_NAME'],
                                   region_name=env['OS_REGION_NAME'])
        return neutron

    def getKeystoneClient(self):

        keystone = ksclient.Client(auth_url=env['OS_AUTH_URL'],
                           username=env['OS_USERNAME'],
                           password=env['OS_PASSWORD'],
                           tenant_name=env['OS_TENANT_NAME'],
                           region_name=env['OS_REGION_NAME'])
        return keystone

    def getGlanceClient(self):

        keystone = self.getKeystoneClient();
        glance_endpoint = keystone.service_catalog.url_for(service_type='image')
        glance = glclient.Client(glance_endpoint, token=keystone.auth_token)
        return glance

    def getCeilometerClient(self):

        cclient = cl.get_client( '2',
							username=env['OS_USERNAME'],
							password=env['OS_PASSWORD'],
							tenant_name=env['OS_TENANT_NAME'],
							auth_url=env['OS_AUTH_URL'])
        return cclient