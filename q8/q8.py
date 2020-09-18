import sys
import os

if len(sys.argv) != 2:
	print("invalid arguments...")
	exit()

path = os.getcwd()
path = os.path.join(path, sys.argv[1])
#print(path)

boys_list = open(path, "r").read().split(' ')
#print(boys_list)

dick={}

for boy in boys_list:
	if boy in dick:
		dick[boy] += 1
	else:
		dick[boy] = 1

#print(dick)
count = 0
simp = ""

for boy in dick:
	if dick[boy] > count:
		count = dick[boy]
		simp = boy

print(simp)