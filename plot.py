#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:24:43 2017

@author: simoncui
"""
#Claim functions used in the program
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,7))

#Load data from files
time , mass = np.loadtxt("heating-2.csv",delimiter=",",unpack=True)

#Calculate the numerator and denominator for the calculation of gradient
numerator = np.sum((time - np.mean(time))*mass)
denominator = np.sum((time - np.mean(time))**2)

#Calculate the gradient and y-intercept
m = numerator / denominator
c = np.mean(mass) - m * np.mean(time)

#Prepare values of d_i, D and sum of d_i
di =  mass - m * time - c
sum_di2 = np.sum(di**2)
D = np.sum((time - np.mean(time))**2)

#Calculate uncertainty of m and c
delta_m = np.sqrt((sum_di2)/(D*(len(time)-2)))
delta_c = np.sqrt((1/len(time)+((np.mean(time))**2/(D)))*((sum_di2)/(len(time)-2)))

#Generate a scatter plotting of data on the graph
plt.scatter(time,mass,label="Data")

#Generate a line with calculated gradient and interception
x = np.linspace(0,np.max(time),1000)
y = x * m + c
plt.plot(x,y,label="Line best fit")

#Putiing labels and the title
plt.title("Plotting of mass loss of\n liquid nitrogen in a heating system")
plt.xlabel("time / second")
plt.ylabel("mass / g")
plt.xlim(0,np.max(time))
plt.ylim(np.min(mass)*0.99,np.max(mass)*1.01)
plt.legend(loc="best")
plt.grid()
plt.savefig("Plot_heating_2")
plt.show()
#Output of gradient and interception
print("The line with gradient of {0:.9E} and y-intercept is at {1:.9E} .".format(m,c))
print("The uncertainty in gradient is {0:.0E} and in interception is {1:.0E}.".format(delta_m,delta_c))

#Save the graph as file
#plt.savefig("Plot_heating_2")
