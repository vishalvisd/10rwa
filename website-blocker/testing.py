from datetime import datetime

blockOnTime="9:00:00"
blockOffTime="16:00:00"
datetimeFormat = "%H:%M:%S"
nextHop = datetime.strptime(blockOffTime, datetimeFormat) - datetime.strptime(blockOnTime, datetimeFormat)
print(type(nextHop))
print(nextHop.seconds)

currentTime = datetime.now()
if currentTime > datetime.strptime(blockOnTime, datetimeFormat):
    print("greater")