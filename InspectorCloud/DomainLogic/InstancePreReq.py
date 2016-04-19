#!/usr/bin/env python
from Authentication import *

class InstancePreReq:

    def __init__(self):

        self.aObj = Authentication("yess");
        self.nova = self.aObj.getComputeClient();
        self.neutron = self.aObj.getNeutronClient();
        self.keystone= self.aObj.getKeystoneClient();
        self.glance = self.aObj.getGlanceClient();
        self.cclient = self.aObj.getCeilometerClient();

    def getAllFlavours(self):

        obj= self.nova.flavors.list();
        flvrs=[];

        for each in obj:
            flvrs.append(each.name);

        return flvrs;

    def getAllImages(self):

        obj= self.nova.images.list();
        imgz=[];

        for each in obj:
            imgz.append(each.name);

        return imgz;

    def getAllNetworks(self):

        obj= self.nova.networks.list();
        netwrk=[];

        for each in obj:
            netwrk.append(each.label);

        return netwrk;

    def getKeypairsList(self):

        obj= self.nova.keypairs.list();
        keyz=[];

        for each in obj:
            keyz.append(each.name);

        return keyz;

    def getSecurityList(self):

        obj= self.nova.security_groups.list();
        scrty=[];

        for each in obj:
            scrty.append(each.name);

        return scrty;
