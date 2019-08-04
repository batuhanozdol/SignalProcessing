# -*- coding: utf-8 -*-

import numpy as np
# for the first system in Question 4

# x[n] is shifted by 10 to convolve it with np.convolve function
x1 = [1,0,0,0,0,0,0,0,0,0,-2,0,0,0,1]
# defined n for h[n] -3<=n<=3
n1 =  np.arange(-6,7)
# h[n] cos(np.pi/3n)
h1 = np.cos((np.pi/3)*n1)
# y[n]=x[n]*h[n]
y1 = np.convolve(x1,h1)
print("First system y[n]=\n",y1)
print()
print()


#for the second system in Question 4
# defining x[n] by looking its convolution plot
x2 = [0,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0]
#defining h[n] by looking its convolution plot
h2 = [0,0,-1,0,1,2,3,2,1,0,-1,0,0]
# y[n]=x[n]*h[n]
y2 = np.convolve(x2,h2)
print("Second system y[n]=\n",y2)
print()
print()


# for the third system in Question 4
# defined a variable as 2
a = 2
# x[n] formulas for each value of n 
x3 = [(2*a**3-2*a**2)/a-1,(2*a**4-2*a**2)/a-1,(2*a**5-2*a**2)/a-1,(2*a**6-2*a**2)/a-1,
      (2*a**7-2*a**2)/a-1,(2*a**8-2*a**2)/a-1,(2*a**9-2*a**2)/a-1,(2*a**10-2*a**2)/a-1,
      (2*a**11-2*a**2)/a-1,(2*a**12-2*a**2)/a-1,(2*a**13-2*a**2)/a-1,(2*a**13-2*a**2)/a-1,
      (2*a**13-2*a**2)/a-1,(2*a**13-2*a**2)/a-1,(2*a**13-2*a**3)/a-1,(2*a**13-2*a**4)/a-1,
      (2*a**13-2*a**5)/a-1,(2*a**13-2*a**6)/a-1,(2*a**13-2*a**7)/a-1,(2*a**13-2*a**8)/a-1,
      (2*a**13-2*a**9)/a-1,(2*a**13-2*a**10)/a-1,(2*a**13-2*a**11)/a-1,(2*a**13-2*a**12)/a-1]
h3 = [0,-1,-2,-3,-2,-1,0,0,0,0,0,0,1,2,3,2,1]
y3 = np.convolve(x3,h3)
print("Third system y[n]=\n",y3)