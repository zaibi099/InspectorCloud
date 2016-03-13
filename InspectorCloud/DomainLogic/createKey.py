#!/usr/bin/env python
import sys
import datetime
import time
from Authentication import *

class createKey:

    def __init__(self):

        self.aObj = Authentication("msssg");
        self.nova = self.aObj.getComputeClient();
        self.neutron = self.aObj.getNeutronClient();
        self.keystone = self.aObj.getKeystoneClient();
        self.glance = self.aObj.getGlanceClient();
        self.cclient = self.aObj.getCeilometerClient();

    def createKeyPlease(self):

        keypair_name = "maKey";
        self.nova.keypairs.list();
        ts = time.time();
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S');
        stri = keypair_name+st;
        print stri;
        self.nova.keypairs.create(name=stri)

    def getKeypairsList(self):

        obj = self.nova.keypairs.list();
        keyz = [];
        for each in obj:
            keyz.append(each.name);
        return keyz;


obj = createKey();
obj.createKeyPlease();