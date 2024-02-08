#------------- Design Pattern 1 -----------------
import time

#--Closures
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# full_name = outer_function("Manish")
# print(full_name(" Rai"))


# Decorator in Python

def log_calls(func):
    def wrapper(*args,**kwargs):
        now = time.time()
        print("Calling {0} with {1} and {2}.".format(func.__name__,args,kwargs))
        return_value = func(*args,**kwargs)
        print("Executed {0} with {1}".format(func.__name__,time.time()-now))
        return return_value
    return wrapper

def test1(a,b,c):
    print("\tCalled test1.")

def test2(a,b):
    print("\tCalled test2.")

def test3(a,b):
    print("\tCalled test3.")
    time.sleep(1)

# test1 = log_calls(test1)
# test2 = log_calls(test2)
# test3 = log_calls(test3)

# test1(7,5,9)
# test2(5,b=1)
# test3(a=4,b=6)