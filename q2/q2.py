from functools import reduce
def colapse(L):
    temp=map(lambda x: reduce(lambda a,b: a+' '+b,x) ,L)
    return reduce(lambda x,y: x+' '+y,temp)

L= [ ["this","is"], ["an", "interesting", "python"], ["programming", "exercise."] ]
print(colapse(L))