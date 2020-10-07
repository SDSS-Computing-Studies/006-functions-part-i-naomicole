#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""

def largest(n):
    n.sort()
    answer=n[-1]
    return answer

x=largest([3,6,1,4,2])
print(x)
