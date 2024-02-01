# ------------------- String and Serialization --------------------------

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
