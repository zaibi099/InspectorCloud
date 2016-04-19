import glob
import re
import sys
import os
import itertools
import datetime
i = datetime.date.today()

str='{0.year}-{0.month}-{0.day}'.format(i)   
ceilometerFiles=glob.glob("/opt/stack/logs/ceilometer*.log")
# print ceilometerFiles
# print len(ceilometerFiles)
index=0
alreadyRead0=0
alreadyRead1=0
fileName="/opt/stack/logs/ceilometer-alarm-evaluator.log"
# print fileName
for i in ceilometerFiles:
#     if i=='/opt/stack/logs/ceilometer-aipmi.log':
#     if i=='/opt/stack/logs/ceilometer.log':
#     if i=='/opt/stack/logs/ceilometer-collector.log.2015-12-20-120024':
    if i==fileName:
        break;
    else:
        index=index+1
out=open(ceilometerFiles[index],'r')
# print out.name

# a=out.readline()
# print a
out=open(ceilometerFiles[index],'r')
# print out.name
out.seek(0,2)
alreadyRead1=0
alreadyRead1=out.tell()
if(alreadyRead1>alreadyRead0):
	print "alreadyRead0 before read:",alreadyRead0
	out.seek(0,0)
	file=out.readlines()
	alreadyRead0=out.tell()
	print "alreadyRead0 after read:",alreadyRead0
	#         for i in file:
	#             print i
	#             print"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"


	# uncomment

	matchingError0 = [s for s in file if(re.search(r"\d.\bERROR\b", s))]
	matchingWarning0 = [s for s in file if(re.search(r"\d.\bWARNING\b", s))]



	# print '#############################################MATCHED ERRORS#######################################################'
	# for i in range(0,len(matchingError0),1):
	    # print matchingError0[i]
	# print "No of errors",len(matchingError0)
	# print '#############################################MATCHED WARNINGS###################################################'
	# for i in range(0,len(matchingWarning0),1):
	    # print matchingWarning0[i]
	# print "No of warnings",len(matchingWarning0)
	out.close()