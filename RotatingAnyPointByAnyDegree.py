
import math
import matplotlib.pyplot as plt
import tkinter

x=int(input("Enter the value of X\n"))
y=int(input("Enter the value of Y\n"))

angle=int(input("Enter the rotating angle in degree\n"))

p=(x,y)


plt.scatter(p[0],p[1],label="before rotation")

X1=(p[0] * math.cos ((angle*math.pi)/180 ) ) - p[1] * math.sin((angle*math.pi)/180)
Y1=(p[0]* math.sin((angle*math.pi)/180) )+ (p[1] *  math.cos ((angle*math.pi)/180 ) )

plt.scatter(X1,Y1,label="after rotation")
plt.legend()
plt.show()
