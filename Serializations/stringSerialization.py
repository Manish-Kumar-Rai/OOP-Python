# ------------------- String and Serialization --------------------------
import datetime
import sys
import re
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

