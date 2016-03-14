#!/usr/bin/env python
import sys
from Authentication import *


class makeBillPreReq:
    def __init__(self, arguments):

        self.aObj = Authentication("yess");
        self.nova = self.aObj.getComputeClient();
        self.neutron = self.aObj.getNeutronClient();
        self.keystone = self.aObj.getKeystoneClient();
        self.glance = self.aObj.getGlanceClient();
        self.cclient = self.aObj.getCeilometerClient();ch

    def getAllMetersName(self):

        tenantList = self.keystone.tenants.list(limit=None, marker=None)
        metersDict = {}
        list1 = []
        meterList = []
        name = ''

        for each1 in tenantList:
            if (each1.name == 'admin'):
                query0 = [dict(field='project_id', op='eq', value=each1.id)]
                list1 = self.cclient.meters.list(q=query0, limit=2000)

        temp = []

        novaMeters = []
        for each in list1:
            name = self.getServiceName(each.name)
            if (name == 'nova'):
                temp.append(each.name)

        novaMeters = list(set(temp))
        # return novaMeters;