#!/usr/bin/env python
import sys
from AlarmGenerate import *

args=[];

for arg in sys.argv:
    args.append(arg);
    print arg

alarmObj = AlarmGenerate(args);
alarmObj.createThreshAlarm();