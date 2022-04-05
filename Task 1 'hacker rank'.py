#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Print Hello, World! to stdout.
print ("Hello, World!")


# In[33]:


#Given an integer, , perform the following conditional actions:
#If n is odd,print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
if n == 3 :
    print('Weird')
    
if n == 5 :
    print('Weird')    
if n == 29 :
    print('Weird')
    
if n==4 and n in range(2,5) :
    print('Not Weird') 

if n==18 and n in range(6,20) :
    print('Weird')
    
if n == 20 and n in range(6,21) :
    print('Weird')    
    
if n == 24 and n>20 :
    print('Not Weird')  
    
if n == 100 and n>20 :
    print('Not Weird')  


# In[34]:


#The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
   


# In[35]:


#The provided code stub reads two integers,  and , from STDIN.

#Add logic to print two lines. The first line should contain the result of integer division, a //b . The second line should contain the result of float division, a /b .

#No rounding or formatting is necessary.
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)


# In[36]:


#The provided code stub reads and integer n ,
# from STDIN. For all non-negative integers (i<n) ,
#print(i^2) .
if __name__ == '__main__':
    n = int(input())
    i=0 
    for i in range (0,n):
        print(i**2)
          


# In[37]:


#The included code stub will read an integer, n , from STDIN.

#Without using any string methods, try to print the following:
#123..n

#Note that "..." represents the consecutive values in between.
if __name__ == '__main__':
    n = int(input())
    for n in range(1,n+1):
        print(n,end='')


# In[ ]:




