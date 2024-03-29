# ------------------- String and Serialization --------------------------
import datetime
import sys
import re
import os
import pathlib
import pickle
import json
from typing import Any

from urllib.request import urlopen
from threading import Timer
#------String---------

#--String Manipulation
a = "Manish"
b = """multiline
string""" 
c = ("Three ""string ""together.")
# print(a)
# print(b)
# print(c)

# print(a.istitle())
# print("45\u06602".isdecimal())
# print(float("45\u06602"))
# print(int("45\u06602"))

# count, find, index, rfind, rindex
# myString = "Samastipur"
# print(myString.count("s"))
# print(myString.find("i"))
# print(myString.rfind("i"))
# print(myString.index("i"))
# print(myString.rindex("i"))
# print(myString.find("z"))     #return -1
# print(myString.index("z"))    # raise ValueError

# split, join, replace, partition
s = "Hello world, How are you."
s2 = s.split(" ")
# print(s2)
s3 = "#".join(s2)
# print(s3)
s4 = s3.replace("#","**")
# print(s4)
s5 = s.partition(" ")
# print(s5)


# String Formating

name = "Manish"
activity = "football"
# print("{1}, playing {1}.".format(name,activity))

#escaping braces
classname = "MyClass"
python_code = "print('Hello world')"
template = f"""
public class {classname} {{
    public static void main(Strings[] args){{
        System.out.println("{python_code}")
    }}
}}"""

# print(template)

#f-string can contain python code

email = ("a@example.com","b@example.com")
message = {
    "subject":"You have a Mail!",
    "message":"There is some message in it."
}

formatted = f"""
From: <{email[0]}>
To: <{email[1]}>
Subject: {message["subject"]}
{message["message"]}"""

# print(formatted)

# print(f"{['a' for a in range(5)]}")
# print(f"{'yes' if 'yes' else 'no'}")


# formatting value in string

subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax

# print("Subtotal: ${0}, Tax: ${1:0.2f}, Total: ${total:0.2f}".format(subtotal,tax,total=total))

orders = [("burger", 2, 5), ("fries", 3.5, 1), ("cola", 1.75, 3)]
# print("PRODUCT    QUANTITY    PRICE       SUBTOTAL")
# for product,price,quantity in orders:
#     subtotal = quantity * price
#     print(
#         f"{product:10s}"f"{quantity: ^9d}"f"${price:^8.2f}"f"${subtotal:>5.2f}"
#     )


# print("{the_date:%Y-%m-%d %I:%M%p}".format(the_date = datetime.datetime.now()))

# The Formate method
template = "abc {number:*^10d}"
# print(template.format(number=32))
# print(template.format(number=82))

# Strings are Unicode
characters = b"\x63\x6c\x69\x63\x68\xe9"
# print(characters)
# print(characters.decode("iso8859-5"))

characters = "cliché"

# print(characters.encode("utf-8"))
# print(characters.encode("latin-1"))
# print(characters.encode("CP437"))
# print(characters.encode("ascii","xmlcharrefreplace"))


# print(sys.getdefaultencoding())

#--Mutable bite strings

b = bytearray(b"abcdefgh")
# b[4:6] = b"\x15\xa3"
b[3] = ord(b"g")
b[4] = 68
# print(b)

#-------- FileSystem paths --------------------
path = os.path.abspath(os.sep.join([".","subdir","subsubdir","file.ext"]))
# print(path)

path = (pathlib.Path(".")/"subdir"/"subsubdir"/"file.ext").absolute()
# print(path)

# program to count no. of lines in python code

def count_sloc(dir_path):
    sloc = 0
    for path in dir_path.iterdir():
        if path.name.startswith("."):
            continue
        if path.is_dir():
            sloc += count_sloc(path)
            continue
        if path.suffix != ".py":
            continue
        with path.open() as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    sloc += 1
        return sloc
    
root_path = pathlib.Path(".")


# print(count_sloc(root_path))


#-------------- Serializing Object --------------

some_data = ["a list", "containing", 5,"values including another list",["inner", "list"]]

# with open("pickle_list","wb") as file:
#     pickle.dump(some_data,file)

# with open("pickle_list","rb") as file:
#     loaded_data = pickle.load(file)

# print(loaded_data)
# assert loaded_data == some_data

#--------- Customizing pickles ----------------

class UpdateURL:
    def __init__(self,url):
        self.url = url
        self.contents = ""
        last_updated = None
        self.update()

    def update(self):
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self):
        self.timer = Timer(3600,self.update)
        self.timer.daemon = True
        self.timer.start()

    def __getstate__(self):
        new_state = self.__dict__
        if "timer" in new_state:
            del new_state["timer"]
        return new_state
    
    def __setstate__(self,data):
        self.__dict__ = data
        self.schedule() 

# u = UpdateURL("http://dusty.phillips.codes")
# pickle.dumps(u)

#---------- Serializing web objects- ----------------------

class Contact:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    

class ContactEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,Contact):
            return {
                "is_contact": True,
                "first": obj.first,
                "last": obj.last,
                "full": obj.full_name
            }
        return super().default(obj)
    
def decode_contact(dic):
    if dic.get("is_contact"):
        return Contact(dic["first"],dic["last"])
    return dic

c = Contact("Manish","Rai")
data = json.dumps(c,cls=ContactEncoder)
# print(data)
c2 = json.loads(data,object_hook=decode_contact)
# print(c2.first,c2.last,c2.full_name)

