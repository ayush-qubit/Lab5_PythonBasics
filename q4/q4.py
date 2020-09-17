import itertools as it
#import operator as op

def myFunc(deg, vals, coeffs):
  temp = coeffs
  val1= vals[0]
  val2= vals[1]
  iter = 0

  while(iter<=deg):
    holder = coeffs[iter] * (val2**iter)*(val1**(deg-iter))
    listxy = ""
    listx = 'x*' * (deg-iter)
    listx = listx[0:-1]
    listy = 'y*' * (iter)
    listy = listy[0:-1]
    if listx and listy:
      listxy = listx+'*'+listy
    elif listx:
      listxy = listx
    else:
      listxy = listy
    temp[iter] = listxy + ' -> ' + str(holder)
    iter = iter +1

  
  return temp

