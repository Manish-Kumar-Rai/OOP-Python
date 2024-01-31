#------------ Python Object Oriente Shortcuts -----------------
import sys
import random,string
import datetime, time
# ----------len() function
myList = [4,1,5,6,8,9]
# print(len(myList))

# three ways to return length of an object
class myObj:
    """Retrun length as attribute"""
    def __init__(self):
        self.n = 10

# print(myObj().n)

class myObj2:
    """Return length as magic method."""
    def __len__(self):
        return 10
    
# print(len(myObj2()))
    
class myObj3:
    """Return length as property"""
    def _calculate_length(self):
        return 10
    #oneway to define property
    length1 = property(_calculate_length)

    # another way to define property
    @property
    def length2(self):
        return 12

# print(myObj3().length1)
# print(myObj3().length2)
    
#reversed() function takes __reversed__() method and returns a COPY of that object in reversed order.
    
class MyList:
    def __init__(self,list):
        self.myList = []
        self.n = 0
        for i in list:
            self.myList.append(i)
            self.n += 1

    def __len__(self):
        return self.n
    
    def __getitem__(self,index):
        return self.myList[index]
    
    def __reversed__(self):
        return self.myList[::-1]
    
    def __repr__(self) -> str:
        result = ", ".join(map(str,self.myList))
        return "[" + result +"]"
    
# arr = MyList([1,2,3,4,5,6])
# arr2 = reversed(arr)
# print(arr)
# print(arr2)


normal_list = [1,2,3,4,5]

class CustomSequence:
    def __len__(self):
        return 5
    def __getitem__(self,index):
        return f"x{index}"
    
class FunkyBackwards:
    def __reversed__(self):
        return "BACKWARDS!"
    
# for seq in normal_list, CustomSequence(), FunkyBackwards():
#     print(f"{seq.__class__.__name__}: ",end="")
#     for item in reversed(seq):
#         print(item,",",end="")
#     print()
    
#---Enumerate Function
    
def perfect_num(num):
    i = 0
    sum = 0
    for i in range(1,num//2):
        if num %i == 0:
            sum += i

    if sum == num:
        return True
    else:
        return False
    
# print(perfect_num(8469880908))
    
# filename = sys.argv[1]

# for index, value in enumerate(filename):
#     print(f"{index+1}:{value}")


# print(any([1,2,3,4,"str",None]))
# print(all([1,2,3,4,"str",None]))

contents = ["Ram\n","Bharat\n","Laxman\n","Shatrughan\n"]

try:
    file = open("Ramayan.txt","w")  #write
    file.write(contents[0])
finally:
    file.close()

try:
    file2 = open("Ramayan.txt","a") #append
    for character in contents[1:]:
        file2.write(character)
finally:
    file2.close()

#try (with) object
characters = []
with open("Ramayan.txt","r") as file3:
    for character in file3.readlines():
        characters.append(character)

characters = [character.replace("\n","") for character in characters]

# print(characters)


#my own framework: 
class StringJoiner(list):
    def __enter__(self):
        return self
    
    def __exit__(self,type,value,tb):
        self.result = "".join(self)

with StringJoiner() as joiner:
    for i in range(15):
        joiner.append(random.choice(string.ascii_letters))

# print(joiner.result)

#----------- An alternative to method overloading--------
        
# A function with no arguments
def no_args():
    pass

# A function with an arguments
def mandatory_args(x,y,z):
    pass

# A function with default arguments
def dafault_args(x,y,z,a="some strings",b=False):
    pass

# A function with keyword-only args
def kw_args(x,y="defaultkw",*,a,b="only"):
    print(x,y,a,b)

# kw_args("x","manish",a="a")
    
# we cannot set default values dynamically
number = 5
def funky_fun(number=number):
    print(number)

number = 6
# funky_fun(8)  #8
# funky_fun()  #5
# print(number) #6

# Be careful with empty containers
def hello(b=[]):
    b.append('a')
    print(b)

# hello()
# hello()
# hello()
# hello()
    
#--Variable argument list
    
def arbitrary_args(*args):
    print(args)
    for i in args:
        print(i)

# arbitrary_args("manish","vikas","avinash")
        
# default keyword argument
        
class Options:
    default_options = {
        "port":21,
        "host":"localhost",
        "username":None,
        "password":None,
        "debug":False,
    }

    def __init__(self,**kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self,key):
        return self.options[key]
    

man = Options(username = "Manish",password="123456789",debug=True)
# print(man["username"])
# print(man["password"])
# print(man["debug"])

#Unpacking arguments

def show_args(arg1,arg2,arg3 = "Three"):
    print(arg1,arg2,arg3)

some_args = range(3)
more_args = {
    "arg1":"One",
    "arg2":"Two",
}

# print("Unpacking sequence: ",end="")
# show_args(*some_args)
# print("Unpacking dict: ",end="")
# show_args(**more_args)


# Funtions are object too

def my_function():
    print("The function was called.")

my_function.description = "A silly function"

def second_funtion():
    print("The second function called")

second_funtion.description = "A sillier function"

def another_function(function):
    print("Function description: ",end="")
    print(function.description)
    print("Function name: ",end="")
    print(function.__name__)
    print("Function class: ",end="")
    print(function.__class__)
    print("Now I'll called the function passed in")
    function()

# another_function(my_function)
# print("--------------------------")
# another_function(second_funtion)
# print("--------------------------")

def int_add(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

def string_concate(arr):
    return " ".join(arr)

def add(function,*args):
    return function(args)

# print("Sum: ",add(int_add,4,5,6,7,8,9))
# print("Fullname: ",add(string_concate,"Manish","Kumar","Rai"))

#----------- timed events--------

class TimedEvent:
    def __init__(self,endtime,callback):
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        return self.endtime <= datetime.datetime.now()
    
class Timer:
    def __init__(self):
        self.events = []

    def call_after(self,delay,callback):
        end_time = datetime.datetime.now() + datetime.timedelta(seconds=delay)
        self.events.append(TimedEvent(end_time,callback))

    def run(self):
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
            time.sleep(0.5)


def format_time(message):
    now = datetime.datetime.now()
    print(f"{now:%I:%M:%S} {message}")

def one(timer):
    format_time("Called One.")

def two(timer):
    format_time("Called two.")

def three(timer):
    format_time("Called three.")

class Repeater:
    def __init__(self):
        self.count = 0

    def __call__(self,timer):
        format_time(f"repeat {self.count}")
        self.count += 1
        timer.call_after(5,self)

# timer = Timer()
# timer.call_after(1,one)
# timer.call_after(2,one)
# timer.call_after(2,two)
# timer.call_after(4,two)
# timer.call_after(3,three)
# timer.call_after(6,three)
# repeater = Repeater()
# timer.call_after(5,repeater.repeater)
# format_time("Starting")
# timer.run()
        
# Using function as attributes
class A:
    def print(self):
        print("my class is A.")

def fake_print():
    print("my class is not A.")

# a = A()
# a.print()
# a.print = fake_print
# a.print()


#Monkey patching
class B:
    def __init__(self):
        self.my_list = []

    def add(self):
        self.my_list.append("a")

def monkey_patch(some_object):
    some_object.my_list = []

# b = B()
# b.add()
# b.add()
# b.add()
# b.add()
# print(b.my_list)
# b.add = monkey_patch
# b.add(b)
# print(b.my_list)
    
#---- Callable Objects
    
class Repeater:
    def __init__(self):
        self.count = 0

    def __call__(self,timer):
        format_time(f"repeat {self.count}")
        self.count += 1
        timer.call_after(5,self)

class C:
    def __call__(self,*args):
        return " ".join(args)
    
c = C()
# print(c("Manish","Kumar","Rai"))

