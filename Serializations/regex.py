#--------------- Regular expression ---------------------
import re
import sys

search_string = "hello world"
pattern = "hello world"

match = re.match(pattern,search_string)
# if match:
#     print("Regex match")
# else:
#     print("No match")

#--------

# pattern = sys.argv[2]
# search_string = sys.argv[1]

# match = re.match(pattern,search_string)
# if match:
#     template = "'{}' matches pattern '{}'"
# else:
#     template = "'{}' does not match pattern '{}'"

# print(template.format(search_string,pattern))


pattern = "^(([0-9a-z]+)@([a-z]+\.[a-z]{3}))$"
search_string = "vksrai95@gmail.com"

# match = re.match(pattern,search_string)

# if match:
#     domain = match.groups()
#     print(domain)

# re.search() method
# print(re.search("kumar","Manish kumar rai").group())
# print(re.match("^.*kumar.*$","Manish kumar rai").group())

#re.findall() method

# print(re.findall("a.","abacadefagah"))
# print(re.findall("a(.)","abacadefagah"))
# print(re.findall("(a)(.)","abacadefagah"))
# print(re.findall("((a)(.))","abacadefagah"))

myregex = re.compile("([a-z0-9\.]+)@([a-z\.]+)")

myString = """my email is 'manishkumarrai3389@gmail.com'
my elder brother email is 'vksrai96@yahoo.com'
and my eldest brother email is 'avirai.rai95@gmail.com'."""

# print(myregex.findall(myString))