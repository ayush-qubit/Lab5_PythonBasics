from functools import reduce
def collapse(L):
    temp = map(lambda x: reduce(lambda a,b: a+' '+b, x), L)
    return reduce(lambda x,y: x+' '+y, temp)