from functools import reduce
def A(x):
    return reduce(lambda a,b: a+" "+b, x)

def collapse(L):
    temp=[(lambda x: reduce(lambda a,b: a+" "+b, x))(x) for x in L]
    #temp = map(lambda x: reduce(lambda a,b: a+" "+b, x), L)
    return reduce(lambda x,y: x+' '+y, temp)
