#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""

import math

def hypotenuse(a,b,c):
    if c==True:
        d=(a**2)+(b**2)
        answer= int(math.sqrt(d))
        return answer

    elif c==False:
        myList=[]
        myList.append(a)
        myList.append(b)
        myList.sort()
        n=myList[0]
        m=myList[1]
        p=(m**2)-(n**2)
        answer=math.sqrt(p)
        return answer

x=hypotenuse(13,5,False)
print(x)



