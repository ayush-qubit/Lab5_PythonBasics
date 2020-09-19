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

dic={}

for boy in boys_list:
	if boy in dic:
		dic[boy] += 1
	else:
		dic[boy] = 1

#print(dick)
count = 0
simp = ""

for boy in dic:
	if dic[boy] > count:
		count = dic[boy]
		simp = boy

print(simp)