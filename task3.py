#!python3
"""
Create a function called perimeter()
The input is a list.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""

def perimeter(n):
    answer=sum(n)
    return answer

x=perimeter([1,2,3])
print(x)