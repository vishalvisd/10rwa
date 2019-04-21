#open file
#modify it by first looking through if such a line exists, if exist already don't do anything - case while adding block
#modify it by finding such lines and removing them
#schecule a time to do such operation

#the open command would look for different path for different os.
#so, first we need to also find the os on which the current code would be running

import platform
import os
import time
from datetime import datetime

hostostype = platform.system()

siteToBlock = ['facebook.com', 'twitter.com', "news.google.com"]
websiteToBlock = siteToBlock.copy()

hostFilePath = None

if(hostostype == 'Linux' or hostostype == 'Darwin'):
    hostFilePath = '/etc/hosts'
elif(hostostype == 'Windows'):
    hostFilePath = 'c:/windows/system32/drivers/etc/hosts'

def siteBlocker():
    with open(hostFilePath, 'r') as hostsFile:
        hostFileLines = hostsFile.readlines()
        for i, line in enumerate(hostFileLines):
            host = str(line).split()[1] if len(str(line).split()) > 1 else None
            for site in websiteToBlock:
                if host == site:
                    websiteToBlock.remove(site)
        hostsFile.close()

    with  open(hostFilePath, 'a') as hostsFile:
        print(f"to be appended {str(websiteToBlock)}")
        # append to the file all the remaingin website to block
        for site in websiteToBlock:
            hostsFile.write(f"\n127.0.0.1 {site}")
        hostsFile.close()


def siteUblocker():
    try:
        os.remove('hosts_temp')
    except:
        print("")
    with open(hostFilePath, 'r') as input:
        with open('hosts_temp', 'w+') as output:
            for line in input:
                host = str(line).split()[1] if len(str(line).split()) > 1 else None
                print(f"got host {host}")
                if host not in siteToBlock:
                    print(f"writing back {line}")
                    output.write(line)

    os.remove(hostFilePath)
    os.rename('hosts_temp', hostFilePath)


blockOnTime="12:00:00"
blockOffTime="12:02:00"
datetimeFormat = "%H:%M:%S"
blockOnTimePy = datetime.strptime(blockOnTime, datetimeFormat)
blockOffTimePy = datetime.strptime(blockOffTime, datetimeFormat)
#nextHop = datetime.strptime(blockOffTime, datetimeFormat) - datetime.strptime(blockOnTime, datetimeFormat)

while True:
    currentTime = datetime.now()
    if currentTime > blockOnTimePy and currentTime < blockOffTimePy:
        print("calling site blocker")
        siteBlocker()
        timeToUnblock = blockOffTimePy - currentTime
        print(f"time to unblock", timeToUnblock.seconds)
        time.sleep(timeToUnblock.seconds)
    if currentTime > blockOffTimePy:
        print("calling site unblcker")
        siteUblocker()
        timeToLock = (datetime.strptime("23:59:59", datetimeFormat) - currentTime) + (blockOnTimePy - datetime.strptime("00:00:00", datetimeFormat))
        print(f"time to unblock", timeToLock.seconds)
        time.sleep(timeToLock.seconds)
    time.sleep(5)
