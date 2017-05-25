# -- coding:utf-8 --
# Python v2.7.10
# whologon.py
# Written by Gaearrow

import os
import sys

# Logon Type
logontypedic = {
    0 :'Unknown 0',
    1 :'Unknown 1',
    2 :'Interactive',
    3 :'Network',
    4 :'Batch',
    5 :'Service',
    6 :'Unknown 6',
    7 :'Unlock',
    8 :'NetworkCleartext',
    9 :'NewCredentials',
    10:'RemoteInteractive',
    11:'CachedInteractive',
}


# Process Input
if len(sys.argv) != 2:
    print ''
    print 'Usage: '
    print ''
    print 'wevtutil qe security /format:text /q:"Event[System[(EventID=4624 or EventID=4634)]]" > LogonEvt.dat'
    print ''
    print 'or Save Event-ID 4624,4634 Filtered Log File As Evtlogon.dat by Event Viewer'
    print ''
    print '%s LogonEvt.dat' % sys.argv[0].split('\\')[-1]
    sys.exit(1)
evt = sys.argv[1]
fevt = open(evt,'r')
flogon = open('LogonStat.csv','w')
print >>flogon,'Event No.; Task; Date; Account Name; Account Domain; Logon ID; Logon Type; Workstation Name; Logon Address; Logon Process'

try:
    # Perform the Statistics
    numevent  = 0
    numlogon  = 0
    numlogoff = 0

    # Event source (wevtutil or event viewer save)
    uisaveflag = 0
    resetmark = 'Event['
	
    for eachline in fevt:
        if eachline.find('Task Category') > -1:
            uisaveflag = 1
            resetmark = 'Information\t'		
        if eachline.find(resetmark) > -1:
            # Reset
            evtno    = ''
            task     = ''
            date     = ''
            accname     = ''
            accdomain   = ''
            logonid     = ''
            logontype   = ''
            workname    = ''
            logonaddr   = ''
            logonproc   = ''
            skip = 0
            numevent = numevent + 1
            if uisaveflag == 0:
                evtno = eachline.split('[')[1].split(']')[0]
            else:
                task = 'Logon' if eachline.find('Logon') > -1 else 'Logoff'
                date = eachline.split('Information')[1].split('Microsoft-')[0].strip()
                evtno = numevent
        elif (uisaveflag == 0) and eachline.find('Date:') > -1:
            date = eachline[(eachline.find(':')+1):].strip()
        elif (uisaveflag == 0) and eachline.find('Task:') > -1:
            task = eachline.split(':')[1].strip()
        elif eachline.find('Account Name:') > -1:
            accname = eachline.split(':')[1].strip()
        elif eachline.find('Account Domain:') > -1:
            accdomain = eachline.split(':')[1].strip()
        elif eachline.find('Logon ID:') > -1:
            logonid = eachline.split(':')[1].strip()
        elif eachline.find('Logon Type:') > -1:
            ltnum = int(eachline.split(':')[1])
            logontype = logontypedic[ltnum]
            if ltnum in [5]:  ## reduce logon type is 'Service'
                skip = 1
            if (skip == 0) and (task == 'Logoff'):
                print >>flogon,str(evtno)+';'+task+';'+date+';'+accname+';'+accdomain+';'+logonid+';'+logontype+';;;'
                numlogoff = numlogoff + 1
        elif eachline.find('Workstation Name:') > -1:
            workname = eachline.split(':')[1].strip()
        elif eachline.find('Source Network Address:') > -1:
            logonaddr = eachline[(eachline.find(':')+1):].strip()
        elif eachline.find('Logon Process:') > -1:
            logonproc = eachline.split(':')[1].strip()
            if (task == 'Logon') and (skip == 0):
                print >>flogon,str(evtno)+';'+task+';'+date+';'+accname+';'+accdomain+';'+logonid+';'+logontype+';'+workname+';'+logonaddr+';'+logonproc
                numlogon = numlogon + 1

    fevt.close()
    flogon.close()

    # Print Summary Infomation
    print '============================='
    print 'Summary Information'
    print 'Logon  Event : ',numlogon
    print 'Logoff Event : ',numlogoff
    print 'Total  Event : ',numevent
    print '============================='
    print 'Save Logon Event to '+os.getcwd()+'\LogonStat.csv'


except Exception as e:
    print 'Error: %s' % e
    sys.exit(1)

