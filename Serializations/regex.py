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

pattern = sys.argv[1]
search_string = sys.argv[2]

match = re.match(pattern,search_string)
if match:
    template = "'{}' matches pattern '{}'"
else:
    template = "'{}' does not match pattern '{}'"

print(template.format(search_string,pattern))