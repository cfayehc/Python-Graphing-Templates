# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:45:53 2020

@author: cfay
"""

#function definition


#main


import matplotlib.pyplot as plt
import numpy as np
import math
import csv

x=[]
y=[]
y1=[]
xdata=[]
ydata=[]

with open('data.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        xdata.append(float(row[0]))
        ydata.append(float(row[1]))

p1=plt.scatter(xdata,ydata, marker='o')

#vector = np.vectorize(np.float)
x = np.arange(1, 40000, .5)
#x=np.float(xp)
#x = np.array(list(map(np.float, x)))
#x = vector(x)
R = 200.
C = 1.0E-6
L = 10.0E-3
#y = (x*L)/(R**2*(1-x**2*L*C)**2+(x*L)**2)**(1/2)
y1=(R/(x*L))**2*(1-x**2*L*C)**2+1
y1 = np.array(list(map(np.float, y1)))
y = 1.00/(np.sqrt(y1))

print('Frequency: ', x)
print('Gain: ', y)
 

plt.grid(b=True, which='both', color='0.65', linestyle='-')
plt.plot(x, y)
 
plt.title("Resonance in Parallel LC Oscillator")
plt.xlabel("Frequency")
plt.ylabel("Gain")
plt.show()
plt.savefig('Linearplot.png')


