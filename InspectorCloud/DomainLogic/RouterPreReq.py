from Authentication import *

class RouterPreReq:

    def __init__(self):

        self.aObj = Authentication("yess");
        self.nova = self.aObj.getComputeClient();
        self.neutron = self.aObj.getNeutronClient();
        self.keystone= self.aObj.getKeystoneClient();
        self.glance = self.aObj.getGlanceClient();
        self.cclient = self.aObj.getCeilometerClient();

    def getAllSubnets(self):
        subnets = self.neutron.list_subnets();
        subList=[];

        for each in subnets['subnets']:
            subList.append(each['name']);

        return subList;

    def getAllTenants(self):
        
        tenants = self.keystone.tenants.list();

        tenNames=[];
        
        for each in tenants:
            tenNames.append(each.name);

        return tenNames;

    def getAllNetworks(self):

        obj= self.nova.networks.list();
        netwrk=[];

        for each in obj:
            netwrk.append(each.label);

        return netwrk;