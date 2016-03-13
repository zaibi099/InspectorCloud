import glob
import re
import sys
import os
import itertools
import datetime
class Debugging:
    def _init_(self,msg):
        print msg
    def getAllFiles(self):
        ceilometerFiles=glob.glob("/opt/stack/logs/ceilometer*.log")
        return ceilometerFiles

    def getErrorsDict(self):
        ceilometerFiles=self.getAllFiles()
        index=0
        alreadyRead0=0
        alreadyRead1=0
        errorsList=[]
        errorsDict={}
        fileName="/opt/stack/logs/ceilometer-alarm-evaluator.log"
        for i in range(0,len(ceilometerFiles)):
            out=open(ceilometerFiles[i],'r')
            # print "==============================================================="
            # print out.name
            out.seek(0,2)
            alreadyRead1=0
            alreadyRead1=out.tell()
            if(alreadyRead1>alreadyRead0):
                # print "alreadyRead0 before read:",alreadyRead0
                out.seek(0,0)
                file=out.readlines()
                alreadyRead0=out.tell()
                # print "alreadyRead0 after read:",alreadyRead0
                matchingError0 = [s for s in file if(re.search(r"\d.\bERROR\b", s))]
            errorsDict.update({out.name: matchingError0})
            alreadyRead0=0
            alreadyRead1=0
            out.close()
        return errorsDict

    def getWarningsDict(self):

        ceilometerFiles=self.getAllFiles()
        index=0
        alreadyRead0=0
        alreadyRead1=0
        fileName="/opt/stack/logs/ceilometer-alarm-evaluator.log"
        warningList=[]
        warningsDict={}
        for i in range(0,len(ceilometerFiles)):
            out=open(ceilometerFiles[i],'r')
            # print "==============================================================="
            # print out.name
            out.seek(0,2)
            alreadyRead1=0
            alreadyRead1=out.tell()
            if(alreadyRead1>alreadyRead0):
                # print "alreadyRead0 before read:",alreadyRead0
                out.seek(0,0)
                file=out.readlines()
                alreadyRead0=out.tell()
                # print "alreadyRead0 after read:",alreadyRead0
                # print "alreadyRead0 after read:",alreadyRead0
                matchingWarning0 = [s for s in file if(re.search(r"\d.\bWARNING\b", s))]
            warningsDict.update({out.name: matchingWarning0})
            alreadyRead0=0
            alreadyRead1=0
            out.close()
        return warningsDict
# obj1=Debugging()
# errorsDict=obj1.getErrorList()
# warningDict=obj1.getWarningList()
# print errorsDict
# print "*********************************************************"
# print warningDict
# print '#############################################MATCHED ERRORS#######################################################'
# for i in range(0,len(matchingError0),1):
#     print matchingError0[i]
# print "No of errors",len(matchingError0)
# print '#############################################MATCHED WARNINGS###################################################'
# for i in range(0,len(matchingWarning0),1):
#     print matchingWarning0[i]
# print "No of warnings",len(matchingWarning0)

