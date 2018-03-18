import sys
import math
l=[3,1,4,8,7,5,0,3,6,4,1,7,4]
max= -float('inf')
second=-float('inf')
for i in l:
    if i>max:
        second=max
        max=i
    elif second<i:
         second=i
         

        
print (max)
print (second)
