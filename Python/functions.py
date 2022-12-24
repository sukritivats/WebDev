# input and print func are in built functions

# to define a userdefined function we have to use def keyword followed by function name along with parameters
def square(x):
    return x*x
def cube(x):
    return x*x*x

for i in range (10):
    print(f"the square of {i} is {square(i)}")
