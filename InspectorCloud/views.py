#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

from django.shortcuts import render
from django.shortcuts import *
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
import os
import time
import subprocess

#%%%%%%%%%%%%%%%%%%%%%% ZAIBI's %%%%%%%%%%%%%%%%%%%%%%%%%%%

from DomainLogic.InstancePreReq import *
from DomainLogic.makeBillPreReq import *
from DomainLogic.preReq import *
from DomainLogic.AlarmPreReq import *
from DomainLogic.RouterPreReq import *
from DomainLogic.createBillCategory import *
from DomainLogic.MongoDatabase import *
from DomainLogic.BillGeneratePreReq import *
from DomainLogic.GenerateBill import *
from DomainLogic.Stats import *

#%%%%%%%%%%%%%%%%%%%%% Umar's %%%%%%%%%%%%%%%%%%%%%%%%%%%%

from DomainLogic.RunningInstances import *
from DomainLogic.Debugging import *
from DomainLogic.SampleList import *
from DomainLogic.ResourcesQuotas import *
from DomainLogic.Events import *
#%%%%%%%%%%%%%%%%%%%%%%% Gloval Var's %%%%%%%%%%%%%%%%%%%%%%%%%%

dlDr="~/fyp/PycharmProjects/Project/InspectorCloud/DomainLogic";

def registerUser(request):

	# if(request.method == 'POST'):
		
	# 	try:
	# 		if( request.method=='POST' ):
				
	# 			print "** REGISTER USER **"
				
	# 			name = request.POST.getlist('name')
	# 			user_name = request.POST.getlist('user_name_2')
	# 			password = request.POST.getlist('password_2')
	# 			email = request.POST.getlist('email')
	# 			phone = request.POST.getlist('phone')
	# 			occupation = request.POST.getlist('occupation')
	# 			location = request.POST.getlist('location')

	# 			print name,user_name,password,email,phone,occupation,location

	# 			t = loader.get_template('InspectorCloud/loginForm.html')
	# 			return HttpResponse(t.render(None,request));
		
	# 	except:
			
	# 		stri = 'exception...Error'
	# 		return HttpResponse(stri)
		
	template = "InspectorCloud/loginForm.html"
	return render(request, template,None)

def loginForm(request):

	if(request.method == 'POST'):
		
		try:
			print "** LOGIN USER **"
				
			user_name = request.POST.get('user_name')
			password = request.POST.get('password')

			print user_name,password

			obj = MongoDatabase();
			flag = obj.verifyUserLogin(user_name,password);

			if flag==True:
				t = loader.get_template('InspectorCloud/index.html')
			else:
				t = loader.get_template('InspectorCloud/loginForm.html')
					
			return HttpResponse(t.render(None,request));
		
		except:
			
			stri = 'exception...Error'
			return HttpResponse(stri)
		
	template = "InspectorCloud/loginForm.html"
	return render(request, template,None)

def index(request):

	template= "InspectorCloud/index.html"
	d=['memory',2,3,"active"]
	return render(request,template,{"foo": d})

def warnings(request):
	
	warningObj1=Debugging()
	warnings=warningObj1.getWarningsDict()
	template="InspectorCloud/warnings.html"
	return render(request,template,{"list": warnings})


def createAlarm(request):

	serverRcvd = ''
	meterRcvd = ''
	comprRcvd = ''
	statsRcvd = ''
	alarmName = ''
	alarmDescrp = ''
	alarmThresh = ''
	alarmTime = ''
	alarmEval = ''

	if(request.method == 'POST'):

		try:
			serverRcvd = request.POST.getlist('instListi')
			meterRcvd = request.POST.getlist('meterList')
			compRcvd = request.POST.getlist('compList')
			statsRcvd = request.POST.getlist('statsList')
			alarmName = request.POST.get('name', '')
			alarmDescrp = "thisAlarmDecription";
			alarmThresh = request.POST.get('thresh', '')
			alarmTime = request.POST.get('timePrd', '')
			alarmEval = request.POST.get('alarmEval', '')
			insufficAction = request.POST.get('insufficAction', '')
			okAction = request.POST.get('OKAction', '')
			alarmAction = request.POST.get('alarmAction', '')

			# print 'ser -> ', serverRcvd[0]
			# print 'mtr -> ', meterRcvd[0]
			# print 'mtr -> ', compRcvd[0]
			# print 'mtr -> ', statsRcvd[0]
			# print 'mtr -> ', alarmName
			# print 'mtr -> ', alarmDescrp
			# print 'mtr -> ', alarmThresh
			# print 'mtr -> ', alarmTime
			# print 'mtr -> ', alarmEval
			# print 'mtr -> ', insufficAction
			# print 'mtr -> ', okAction
			# print 'mtr -> ', alarmAction

			stri=dlDr;
			stri = stri+"/./createAlarmCall.py {} {} {} {} {} {} {} {} {} {} {} {}".format(
				serverRcvd[0], alarmName, alarmDescrp, meterRcvd[0], alarmThresh, compRcvd[0], statsRcvd[0],
				alarmTime, alarmEval, insufficAction, okAction, alarmAction);
			
			subprocess.Popen(stri, stdout=subprocess.PIPE, shell=True)
			print '** CALL GONE ** '

			t = loader.get_template('InspectorCloud/index.html')
			return HttpResponse(t.render(None,request));
		
		except:

			stri = 'exception...Error'
			return HttpResponse(stri)

	alarmObj = AlarmPreReq()
	comp_opr = alarmObj.getAllComparisonOperators()
	stats = alarmObj.getAllStats()
	sers = alarmObj.getInstances()
	novaMeters = alarmObj.getAllMeters()

	template = 'InspectorCloud/createAlarm.html'
	return render(request, template, {
		'comp_opr': comp_opr,
		'stats': stats,
		'servers': sers,
		'meterss': novaMeters,
		})


def alarmList(request):

    obj = AlarmPreReq();
    alList = obj.getAllAlarmList();
    alList = obj.getAllMetersValues(alList);

    template = "InspectorCloud/alarmList.html"
    return render(request, template, {"alarmList": alList})


def createBill(request):

    try:

        if (request.method == 'POST'):

            price = request.POST.getlist("prici[]","");
            billName = request.POST.get("nami","");
            flvrs = request.POST.getlist("flvr[]","");

            print(len(price))
            print(len(flvrs))

            for each in price:
            	print "price  -->",each

            for each1 in flvrs:
            	print "flvrs  -->",each1

            print "billName -> ",billName;

            obj = createBillCategory(billName,flvrs,price);
            obj.saveBillCategory();

            t = loader.get_template('InspectorCloud/index.html')
            return HttpResponse(t.render(None, request));

    except OverflowError:

    	print sys.exc_info()[0]
        return HttpResponse("ERROR.....")
    
    template = "InspectorCloud/createBill.html"
    billObj = makeBillPreReq();
    flvrs = billObj.getAllFlavours();
    return render(request, template, {"flvrs": flvrs})

def generateBill(request):

    try:

        if (request.method == 'POST'):

            catg = request.POST.getlist("category","");
            instance = request.POST.getlist("instances","");

            print "catg -> ", catg[0]
            print "inst -> ", instance[0]

            obj = GenerateBill(catg[0],instance[0]);
            retObj = obj.generateBillPlease();
            myFlvr = obj.getFlavourName();
            price = obj.getCategoryPrice();

            tax = obj.getTaxAmount(retObj['amount']);
            sumi = obj.getTotal(retObj['amount'],tax);
            
            print "Fvlr ->" , myFlvr;
            print "price ->",price

            billObj = makeBillPreReq();
            flvrDetails = billObj.getMyFlavourDetails(myFlvr);

            template = "InspectorCloud/invoice.html";
            return render(request, template,{"catg": catg[0],"sumi":sumi,"tax":tax,"price":price,"inst":instance[0],"billObj":retObj,"flvr":flvrDetails})

    except OverflowError:
        
        return HttpResponse("ERROR.....")

    obj = BillGeneratePreReq();
    cats = obj.getAllBillsCategories();
    alarmObj = AlarmPreReq();
    inst = alarmObj.getInstances();
    
    template = "InspectorCloud/generateBill.html"
    return render(request, template, {"cats": cats,"servers":inst})


def invoice(request):

    template = "InspectorCloud/invoice.html"
    return render(request, template, {"cats": cats,"servers":inst})

def createInstance(request):
	
	try:
		if(request.method == 'POST'):

			key = request.POST.getlist("keysList", "")
			flvr = request.POST.getlist("FlavorList", "")
			img = request.POST.getlist("imagesList", "")
			ntwrk = request.POST.getlist("networkList", "")
			scr = request.POST.getlist("securityList", "")
			name = request.POST.get("instanceName", "")

			stri=dlDr;
			stri = stri+"/./createInstanceCall.py {} {} {} {} {} {}".format(flvr[0], ntwrk[0], img[0], scr[0], key[0], name)
			subprocess.Popen(stri, stdout = subprocess.PIPE, shell = True)

			t = loader.get_template('InspectorCloud/index.html')
			return HttpResponse(t.render(None, request));

	except:

		return HttpResponse("ERROR.....")

	instObj = InstancePreReq();
	flvrs = instObj.getAllFlavours()
	imgz = instObj.getAllImages()
	netwrk = instObj.getAllNetworks()
	keyz = instObj.getKeypairsList()
	scrty = instObj.getSecurityList()

	template = "InspectorCloud/createInstance.html"
	return render(request, template, {
	    "flvrs": flvrs,
	    "imgz": imgz,
	    "netwrk": netwrk,
	    "keyz": keyz,
	    "scrty": scrty
	})


def createRouter(request):

    try:

        if (request.method == 'POST'):

            ten = request.POST.getlist("tenantList", "")
            sub = request.POST.getlist("subnetList", "")
            net = request.POST.getlist("networkList", "")
            name = request.POST.get("routerName", "")

            print ten[0]
            print sub[0]
            print net[0]
            print name

            stri=dlDr;
            stri = stri+"/./createRouterCall.py {} {} {} {}".format(ten[0],net[0],sub[0],name);
            subprocess.Popen(stri, stdout=subprocess.PIPE, shell=True)
            
            t = loader.get_template('InspectorCloud/index.html')
            return HttpResponse(t.render(None, request));

    except:
        return HttpResponse("ERROR.....")

    template = "InspectorCloud/createRouter.html"
    
    rtrObj = RouterPreReq();
    nets = rtrObj.getAllNetworks();
    tenants = rtrObj.getAllTenants();
    subs = rtrObj.getAllSubnets();
    
    return render(request, template, {"nets": nets, "tenants": tenants, "subnets" : subs})




def resourcesQuotas(request):

    tenantsNames=[]
    selectedTenant=""
    template="InspectorCloud/resourceQuotas.html"
    selectedTenant="admin"
    obj1=ResourcesQuotas("")

    tenantsNames=obj1.getTenantsNames()
    obj1.getAllResources(selectedTenant)
    print request.method
    # if (request.method == 'POST'):
    #     try:
    #         selectedTenant=request.POST.get("drop1","")
    #         obj1.getAllResources(selectedTenant)
    #     except:
    #         i=0
    print "selected:",selectedTenant

    return render(request,template,{"foo":obj1,"tenantsNames":tenantsNames})

def runningVms(request):
    obj1=RunningInstances("umar")
    instancesDict=obj1.getRunningInstanceList()
    # for each in instancesDict:
    #     print each
    #     print "\n"
    template="InspectorCloud/runningVms.html"
    return render(request,template,{"foo":instancesDict})

def happenings(request):
    eventObj1=Events()
    eventList=eventObj1.getEventsList('admin')
    # for each in eventList:
    #     print each
    #     print "\n"

    template="InspectorCloud/happenings.html"
    return render(request,template,{"foo":eventList})

def stats(request):

    sampleObj1=Stats()
    sampleList=sampleObj1.getSamplesStat('admin')
    template="InspectorCloud/stats.html"
    return render(request,template,{"foo":sampleList})

def warnings(request):
    warningObj1=Debugging()
    warnings=warningObj1.getWarningsDict()
    template="InspectorCloud/warnings.html"
    return render(request,template,{"list": warnings})

def errors(request):
    
    errorObj1=Debugging()
    errors=errorObj1.getErrorsDict()
    template="InspectorCloud/errors.html"
    return render(request,template,{"list": errors})
