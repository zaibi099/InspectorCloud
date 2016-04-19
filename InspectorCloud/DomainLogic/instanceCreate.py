#!/usr/bin/env python
import os
import time
import sys
from Authentication import *

class InstanceCreate:

    def __init__(self,arguments):

        self.aObj = Authentication("yess");
        self.nova = self.aObj.getComputeClient();
        self.neutron = self.aObj.getNeutronClient();
        self.keystone= self.aObj.getKeystoneClient();
        self.glance = self.aObj.getGlanceClient();
        # self.cclient = self.aObj.getCeilometerClient();
        self.args=arguments;

        for each in arguments:
            print "--->",each

    def getNetworkId(self):

        desiredNet = self.args[2];
        print "d--->", desiredNet;
        netId="";
        neti = self.nova.networks.list()

        for each in neti:
            if each.label==desiredNet:
                netId = each.id;

        return netId;

    def getInstanceName(self):
        return self.args[6];

    def createInstance(self):

        flvrName= self.args[1];
        imageName= self.args[3];
        securityGroup = self.args[4];
        keyName= self.args[5];
        instanceName= self.args[6];
        netId = self.getNetworkId();

        print netId;
        stri= "nova boot --flavor {} --image {} --nic net-id={} --security-group {} --key-name {} {}".format(flvrName,imageName,netId,securityGroup,keyName,instanceName)
        os.system(stri);
        time.sleep(7)

    def addSecurityGroups(self):

        try:
            securityGroup = self.args[4];
            group = self.nova.security_groups.find(name=securityGroup);
            self.nova.security_group_rules.create(group.id, ip_protocol="tcp" ,from_port=22, to_port=22);
            self.nova.security_group_rules.create(group.id, ip_protocol="icmp",from_port=-1, to_port=-1);
        except Exception:
            print "Exception raised already exist rule";

    def assignFloatingIp(self):

        floating_ip = self.nova.floating_ips.create(self.nova.floating_ip_pools.list()[0].name);
        ser = self.nova.servers.list();
        print len(ser)
        server=0;

        print self.args[6];

        for each in ser:
            if(each.name==self.args[6]):
                server = each;
                print server.name
            break;

        self.nova.servers.add_floating_ip(server,floating_ip.ip);
        print "Ja bachiyeeaaa Ayashi Maarr...";