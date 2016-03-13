import Authentication

aObj = Authentication("yess");

nova = aObj.getComputeClient();
neutron = aObj.getNeutronClient();
keystone= aObj.getKeystoneClient();
glance = aObj.getGlanceClient();

devLoc = "~/FYP/devstack";

imgz= nova.images.list()
desiredImage = 'cirros-0.3.4-x86_64-uec';
imageId=None;
instanceName = "bazuka";
securityGroup = "default";

#============================================

if imgz is None:
	print 'empty'
else:
	#print 'Something in Images'
	for x in imgz:
		if x.name == desiredImage:
			imageId = x.id;
			imageName = x.name;
			break;

print 'Image ID : ' +imageId;
print 'Image Name : ' +imageName;
print '-';

#==============================================

flvrs= nova.flavors.list()
for obj in flvrs:
    print obj.name;
    
desiredflvr = 'm1.nano';
flvrName=None;

if flvrs is None:
	print 'empty'
else:
	#print 'Something in Flvrs'
	for x in flvrs:
		if x.name == desiredflvr:
			flvrName = x.name;
			break

print 'Flavor Name : ' +flvrName+"\n";

#============================================

neti = nova.networks.list()
desiredNet = 'private';
netId=None;

if neti is None:
	print 'empty'
else:
	#print 'Something in Nets'
	for x in neti:
		if x.label == desiredNet:
			netId = x.id;
			break


#========================= KEYPAIRS
    
key = nova.keypairs.list();
for obj in key:
    print obj.name;
keyName=0;

#========================= SERVERS


ser = nova.servers.list();

for each in ser:
    nova.servers.delete(each);

print "Deleting Existing Servers.....";
time.sleep(10);


#============================ FLOATING IPs

ExistingIps = nova.floating_ips.list();

for obj in ExistingIps:
    print obj.ip;

for each in ExistingIps:
    print "**";
    nova.floating_ips.delete(each);

#============================

for each in key:
    if(each.name=="keyi"):
        print each.name
        keyName=each.name;
        
        stri = "nova boot --flavor "+flvrName+" --image "+imageName+" --nic net-id="+netId+" --security-group "+securityGroup+" --key-name "+keyName+" "+instanceName;  
        
        os.system(stri);
        time.sleep(7)
        
        nova_ips = nova.floating_ip_pools.list();
        floating_ip = nova.floating_ips.create(nova.floating_ip_pools.list()[0].name);
        
        ser = nova.servers.list();
        server=0;
        
        for each in ser:
            if(each.name==instanceName):
                server = each;
                break;
        
        nova.servers.add_floating_ip(server,floating_ip.ip);
        group = nova.security_groups.find(name=securityGroup);
        nova.security_group_rules.create(group.id, ip_protocol="tcp" ,from_port=22, to_port=22);
        nova.security_group_rules.create(group.id, ip_protocol="icmp",from_port=-1, to_port=-1);
        
        break;
    else:
        print "No key found..Generate Key First";
        break;

print "Ja bachiyeeaaa Ayashi Maarr...";

