
def right_just(s):
    print " " * (70 - len(s)), s


def print_dank(aditionalword):
    print "dank", aditionalword, "dank"
 
def do_thrice(fn, param):
    fn(param)
    fn(param)
    fn(param)
 
 
 
 
#main    
#right_just("dankadfadfadfadfaf")

do_thrice(print_dank, raw_input("enter the dankest word: "))

