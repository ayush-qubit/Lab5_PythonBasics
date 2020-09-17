import functools as ft
from itertools import chain

def Fib(n):
  result = list(range(2, n+1))
  temp = result.copy()
  temp = list( map(lambda v : list( filter(lambda w : w !=v and w % v == 0 , temp) ), temp))
  temp = list(set(chain(*temp)))
  result = list(filter(lambda x: x not in temp, result))
  return result
