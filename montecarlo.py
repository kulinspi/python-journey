# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 19:59:37 2018

@author: lenovo
"""

#from random import randrange
import math
import matplotlib.pyplot as plt
import numpy as np
import time
#print (randrange(10))

x,y = 0,0
promien = 0
licznik=0
pusta=0
bokkwadratu=1000
promienkola=bokkwadratu/2




start = time.time()






n=4000



for i in range (n):
    (dx, dy) = ((np.random.random_sample())*bokkwadratu, (np.random.random_sample())*bokkwadratu)
    #print ("wylosowano %d" % dx,dy)
    #print (abs(dx-500),abs(dy-500))
    promien = math.hypot (dx-promienkola,dy-promienkola)
    #print ("%d" % promien)
    if (promien<=promienkola):
        licznik+=1
        
        plt.scatter(dx, dy,  c='r', s = 9)
    else:
       plt.scatter(dx, dy,c='b',s=9)
               
        
end = time.time()    
print("%2.2f"% (end - start))
print (licznik/n*4)
plt.show()
    