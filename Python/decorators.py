# function which return modified version of that current  function

def announce(f): # takes input of hello function
    def wrapper(): # gives a new function
        print("About to run the function...")
        f()
        print("Done with function. ")
    return wrapper

@announce
def hello():  #hello func is wrapped around the decorator announce functions
    print("Hello, python")
hello()

'''
take a function and add capability to it

'''
