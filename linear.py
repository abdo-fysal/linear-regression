# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 22:57:21 2017

@author: aboda
"""
import numpy as np
from matplotlib import pyplot as plt
class LinearRegression:
    x=0
    y=0
    alpha=0
    N=0
    
    def __init__(self,m,n,a,nn):
        self.x=m
        self.y=n
        self.alpha=a
        self.N=nn
        
 
  
   
   
    def Gradient(self,X,Y,ALPHA,iteration):
        
       
      
        theta=np.array([1,1])
        i=iteration
        j=iteration
        err=1
        err1=1
       
        while(i>=0):
            while(j>=0):
                err=(1/self.N)*(theta[0]+theta[1]*self.x[j]-self.y[j])
                err1=(self.x[j]/self.N)*(theta[0]+theta[1]*self.x[j]-self.y[j])
                j=j-1
            
            theta[0]=theta[0]-ALPHA*err
            theta[1]=theta[1]-ALPHA*err1
            i=i-1
        return theta    
               
    def start(self):
        
        t=np.array([1,1])
        h=np.array([0,0,0,0,0,0,0,0,0])
      
        
        t= self.Gradient(self.x,self.y,self.alpha,self.N-1)
        p=self.N-1
        while(p>=0):
            h[p]=t[0]+self.x[p] * t[1]
            p=p-1

            print(h)
            print(t)
        plt.plot(self.x,self.y,'ro',color='black')

        plt.ylabel('price')
        plt.xlabel('size')
        plt.axis([0,600,0,5000])
        plt.plot(self.x,h,'b')
        plt.plot()
        plt.show()
      
      
x1=np.array([112,346,198,305,372,550,302,420,578])
y1=np.array([1120,1523,2102,2230,2600,3200,3409,3689,4460]) 
w=LinearRegression(x1,y1,0.00008,9)   
print(w.x[0])
w.start()        
     
    
    
    