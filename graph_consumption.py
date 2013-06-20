#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

import csv  #excel saved csv
months = []
years = []
kwhs = []
notes = []

with open('excel.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        months.append(row[0:1])
        years.append(row[1:2])
        kwhs.append(row[2:3])
        notes.append(row[3:4])

months = months[1:] # removing header from data
#print(months)
kwhs = kwhs[1:] # removing header from data
#print(kwhs)


def flatten(lst):
    for elem in lst:
        if type(elem) in (tuple, list):
            for i in flatten(elem):
                yield i
        else:
            yield elem

#flattened = list( flatten(kwhs) )
flat_kwh = []
for elem in flatten(kwhs):
    flat_kwh.append(int(elem))

print(flat_kwh)


N = 12
ind = np.arange(N)  # x coor group location
width = 0.12       # bar widths


plt.subplot(111)
kwh_2008 = flat_kwh[:12]
rects1 = plt.bar(ind, kwh_2008, width, color='#FF0000')

kwh_2009 = flat_kwh[12:24]
rects2 = plt.bar(ind+width, kwh_2009, width, color='#FF9933')

kwh_2010 = flat_kwh[24:36]
rects3 = plt.bar(ind+2*width, kwh_2010, width, color='#FFFF00')

kwh_2011 = flat_kwh[36:48]
rects4 = plt.bar(ind+3*width, kwh_2011, width, color='#00FF00')

kwh_2012 = flat_kwh[48:60]
rects5 = plt.bar(ind+4*width, kwh_2012, width, color='#0000FF')

kwh_2013 = flat_kwh[60:72]
rects6 = plt.bar(ind+5*width, kwh_2013, width, color='#FF00FF')

plt.ylabel('kWh')
plt.title('Electricity Consumption')
plt.xticks(ind+width, ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',))

plt.legend( (rects1[0], rects2[0], rects3[0], rects4[0], rects5[0], 
             rects6[0]), (years[1], years[13], years[25], years[37], 
             years[49], years[61]))

'''
def autolabel(rects):
    # text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects5) 
'''

plt.show()
