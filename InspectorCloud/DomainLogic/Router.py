#!/usr/bin/env python
from Authentication import *
import time

class Router:

        def __init__(self,arguments):

            self.aObj = Authentication("yess");
            self.nova = self.aObj.getComputeClient();
            self.neutron = self.aObj.getNeutronClient();
            self.keystone= self.aObj.getKeystoneClient();
            self.glance = self.aObj.getGlanceClient();
            self.cclient = self.aObj.getCeilometerClient();
            self.args=arguments;

        def createRouter(self):

            routerName = self.args[4];
            desiredSubnet = self.args[3];
            desiredNet = self.args[2];
            tenantName = self.args[1];


            if (self.checkDuplicate(routerName,tenantName)==False):
                
                netId=None;
                subnetId=None;
                routerId=None;


                neti = self.nova.networks.list()
                for x in neti:
                    if x.label == desiredNet:
                        netId = x.id;
                        break

                bodyVal= {
                        "router": {
                        "name": routerName,
                        "external_gateway_info":
                            {
                            "network_id": netId,
                            "enable_snat": "True",
                            },
                        "admin_state_up": "true"
                    }
                }

                subnets = self.neutron.list_subnets();
                for each in subnets['subnets']:
                    if each['name'] == desiredSubnet:
                        subnetId = each['id']

                subNeti = {"subnet_id": subnetId}
                self.neutron.create_router(body=bodyVal);
                time.sleep(1);
                rtrLists = self.neutron.list_routers();

                for each in rtrLists['routers']:
                    if each['name'] == routerName:
                            routerId = each['id']
                
                    interfaceArg = {}
                    self.neutron.add_interface_router(routerId,body=subNeti);
                    print "Router Created with name ", routerName
            else:
                print "Router Already Exists for this user"; 

        def checkDuplicate(self,myName,myTenant):

            rtrLists = self.neutron.list_routers();
            tenant = self.keystone.tenants.list();

            for each in tenant:
                if (each.name==myTenant):
                    myId = each.id;

            for each in rtrLists['routers']:
                if ( (each['tenant_id'] == myId) & (each['name'] == myName) ):
                    return True

            return False