import csv
import os, sys
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# csv file name 
filename = "csv_file"
  
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 

  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 

X1=[]
Y1=[]
Z1=[]

for row in rows:
    X1.append(float(row[0]))
    Y1.append(float(row[1]))
    Z1.append(float(row[2]))

  
X = np.array(X1)
Y = np.array(Y1)
Z = np.array(Z1)

fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(projection='3d')
ax.grid(False)
ax.set_xlabel("X axis",weight='bold')
ax.set_ylabel("Y axis",weight='bold')
ax.set_zlabel("Z axis",weight='bold')

surf = ax.plot_trisurf(X, Y, Z,cmap=cm.coolwarm,antialiased = True)
m = cm.ScalarMappable(cmap=cm.coolwarm)
m.set_array(Z)
fig.colorbar(m, ax=ax, shrink=0.5, fraction=0.40)
#fig.colorbar(surf, shrink=0.5)
plt.show()

fig.tight_layout()
fig.savefig('q3plot.jpg', bbox_inches='tight', pad_inches=0.1)
plt.close()

