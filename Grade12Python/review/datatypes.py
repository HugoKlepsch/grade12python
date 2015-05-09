import math
width = 17
height = 12.0
delimiter = "."

#should be 8.5, but because int it is either 8 or 9
#print width / 2

#because float, devides as expected
#print width / 2.0

#no roundng required, should be 4, but is float because one input is float
#print height / 3

#should be 1 + 10, therefore 11
#print 1 + 2 * 5

#should print the string five times, for some reason
#print delimiter * 5

def volumesphere(radius):
    return (4.0/3) * math.pi * (radius ** 3)

def price(copies):
    price = 0.0
    bookprice = 24.95
    discount = .6
    price = price + (bookprice * copies * discount)
    price = price + 3
    for i in range(copies - 1):
        price = price + .75
    return price

def time2secs(hours, mins, secs):
    time = 0.0
    time = time + (hours * 3600)
    time = time + (mins * 60)
    time = time + secs
    return time

def secs2time(secs):
    hours = math.floor(float(secs) / 3600)
    minremain = secs % 3600
    mins = math.floor(minremain / 60)
    secremain = minremain % 60
    print "hours: ", hours
    print "mins: ", mins
    print "secs: ", secremain

#print volumesphere(5)

#print price(60)

jogtime = 0
origtime = time2secs(6, 15, 00)
jogtime = time2secs(0, 8, 15)
jogtime = jogtime + (time2secs(0, 7, 12) * 3)
jogtime = jogtime + time2secs(0, 8, 15)
print "joggingtime: ", jogtime
print "totaltime: ", jogtime + origtime
finaltime = jogtime + origtime
print "Endtime: ", secs2time(finaltime)
