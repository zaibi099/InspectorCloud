from django.shortcuts import render

# Create your views here.
from django.shortcuts import *
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
#from scripts.ceilometer import *
from DomainLogic.RunningInstances import *
from DomainLogic.Debugging import *
#from scripts.ceilometer import *
from DomainLogic.preReq import *
from DomainLogic.AlarmPreReq import *
import os
import subprocess
import time
from DomainLogic.EventList import *
from DomainLogic.SampleList import *
from DomainLogic.InstancePreReq import *

def home(request):

    template= "InspectorCloud/home.html"
    d=['memory',2,3,"active"]
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,template,{"foo": d})

def alarms(request):
    serverRcvd = ""
    meterRcvd = ""
    comprRcvd = ""
    statsRcvd = ""
    alarmName = ""
    alarmDescrp = ""
    alarmThresh = ""
    alarmTime = ""
    alarmEval = ""

    if (request.method == 'POST'):
        try:
            serverRcvd = request.POST.get("drop1", "")
            meterRcvd = request.POST.get("drop2", "")
            compRcvd = request.POST.get("drop3", "")
            statsRcvd = request.POST.get("drop4", "")
            alarmName = request.POST.get("alName", "")
            alarmDescrp = request.POST.get("desci", "")
            alarmThresh = request.POST.get("trhsh", "")
            alarmTime = request.POST.get("alarmTime", "")
            alarmEval = request.POST.get("alarmEval", "")
            insufficAction = request.POST.get("insufficDataAction", "")
            okAction = request.POST.get("okAction", "")
            alarmAction = request.POST.get("alarmAction", "")

            stri = "~/fyp/PycharmProjects/MyProjects/InspectorCloud/DomainLogic/./createAlarmCall.py {} {} {} {} {} {} {} {} {} {} {} {}".format(
                serverRcvd, alarmName, alarmDescrp, meterRcvd, alarmThresh, compRcvd, statsRcvd,
                alarmTime, alarmEval, insufficAction, okAction, alarmAction);
            subprocess.Popen(stri, stdout=subprocess.PIPE, shell=True)
            # alarmChecker = "./alarmChecker.py";
            # os.system(stri);
            # stri = "Do something" + username;
            # time.sleep(5);./
            # subprocess.Popen(alarmChecker,stdout=subprocess.PIPE, shell=True)
            return HttpResponse(stri)
        except:
            stri = "ERROR ./createAlarmCall.py {} {} {} {} {} {} {} {} {} {} {} {}".format(serverRcvd, alarmName,
                                                                                           alarmDescrp, meterRcvd,
                                                                                           alarmThresh, compRcvd,
                                                                                           statsRcvd, alarmTime,
                                                                                           alarmEval, insufficAction,
                                                                                           okAction, alarmAction);

        return HttpResponse(stri)

    template = "InspectorCloud/alarms.html"

    alarmObj = AlarmPreReq();
    comp_opr = alarmObj.getAllComparisonOperators();
    stats = alarmObj.getAllStats();
    sers = alarmObj.getInstances();
    novaMeters = alarmObj.getAllMeters();

    return render(request, template, {"comp_opr": comp_opr, "stats": stats, "servers": sers, "meterss": novaMeters})


def instance(request):
    try:
        if (request.method == 'POST'):

            variabli = request.POST.get("generate_key", "")
            print "--> ", variabli;

            if (variabli == "10"):
            #
                print "in side generate key"
            #     stri = "~/fyp/PycharmProjects/MyProjects/InspectorCloud/DomainLogic/./createKey.py"
            #     subprocess.Popen(stri, stdout=subprocess.PIPE, shell=True)
            #
            #     template = "InspectorCloud/instance.html"
            #     print "--ad-as-das"
            #
            #     instObj = InstancePreReq();
            #     flvrs = instObj.getAllFlavours()
            #     imgz = instObj.getAllImages()
            #     netwrk = instObj.getAllNetworks()
            #     keyz = instObj.getKeypairsList()
            #     scrty = instObj.getSecurityList()
            #
            #     return render(request, template, {"flvrs": flvrs, "imgz": imgz, "netwrk": netwrk, "keyz": keyz, "scrty": scrty})
            # else:

                key = request.POST.get("drop5", "")
                flvr = request.POST.get("drop1", "")
                img = request.POST.get("drop2", "")
                ntwrk = request.POST.get("drop3", "")
                scr = request.POST.get("drop4", "")
                name = request.POST.get("namii", "")

                stri = "~/fyp/PycharmProjects/MyProjects/InspectorCloud/DomainLogic/./createInstanceCall.py {} {} {} {} {} {}".format(
                    flvr, ntwrk, img, scr, key, name)
                subprocess.Popen(stri, stdout=subprocess.PIPE, shell=True)

                t = loader.get_template('InspectorCloud/resourcemonitoring.html')
                return HttpResponse(t.render(None, request));

    except:
        return HttpResponse("ERROR.....")

    template = "InspectorCloud/instance.html"

    instObj = InstancePreReq();
    flvrs = instObj.getAllFlavours()
    imgz = instObj.getAllImages()
    netwrk = instObj.getAllNetworks()
    keyz = instObj.getKeypairsList()
    scrty = instObj.getSecurityList()

    return render(request, template, {"flvrs": flvrs, "imgz": imgz, "netwrk": netwrk, "keyz": keyz, "scrty": scrty})









def resourcemonitoring(request):
    obj1=RunningInstances("umar")
    instancesDict=obj1.getRunningInstanceList()

    template="InspectorCloud/resourcemonitoring.html"
    return render(request,template,{"foo":instancesDict})

def debugging(request):
    template="InspectorCloud/debugging.html"
    d=["bfkldbfkldbfkdbsafkbasdkbfkbadsfbadsfbdas","bfahdsbfdsafkjadskjfdksjbksdajbvkabhaeiurhfuiashdfkjdsbkvasdb"]
    return render(request,template,{"foo":d})

def error(request):
    errorObj1=Debugging()
    errors=errorObj1.getErrorsDict()

    template="InspectorCloud/error.html"
    return render(request,template,{"list": errors})

def warning(request):
    warningObj1=Debugging()
    warnings=warningObj1.getWarningsDict()
    template="InspectorCloud/warning.html"
    return render(request,template,{"list": warnings})

def event(request):
    eventObj1=Events()
    eventList=eventObj1.getEventsList()
    template="InspectorCloud/event.html"
    return render(request,template,{"foo":eventList})

def resourceUsage(request):
    sampleObj1=Samples()
    sampleList=sampleObj1.getSamplesStat()
    template="InspectorCloud/resourceUsage.html"
    return render(request,template,{"foo":sampleList})

def Layout(request):
    template="InspectorCloud/Layout.html"
    return render(request,template)

def makeBillForms(request):
    template="InspectorCloud/makeBillForms.html"
    return render(request,template)