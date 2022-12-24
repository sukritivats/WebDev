'''
result=x/y
print(f"{x}/{y}  = {result}")
when y=0 we will get a excption (error: zero divison error)
when u try to input a string insted of an integer again an excption will be thrown (error: value error)
'''

import sys
try:
    x= int(input("x: "))
    y= int(input("y: "))
except ValueError:
    print("Error!!!! invalid input")  
    sys.exit(1)

try:
    result=x/y
except ZeroDivisionError:
    print("Error !!! cannot divide by zero")
    sys.exit(1)

'''


'''