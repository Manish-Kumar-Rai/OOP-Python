#--------------- The Iterator Pattern ----------------------

import sys
from collections import namedtuple
#-- The iterator Protocol

class CapitalIterable:
    def __init__(self,string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)
    
class CapitalIterator:
    def __init__(self,string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        word = self.words[self.index]
        self.index += 1
        return word
    
    def __iter__(self):
        return self
    

iterable = CapitalIterator("the quick brown fox jumps over the lazy dog.")
iterator = iter(iterable)

# while True:
#     try:
#         print(next(iterator),end=" ")
#     except StopIteration:
#         break


#simple syntax
# for i in iterator:
#     print(i,end=" ")

#------- List Comprehensions --------------------

# def convertToNumber(num):
#     return int(num)
input_strings = ["1", "5", "28", "131", "3"]
# print(input_strings)
# output_integers = map(convertToNumber,input_strings)
output_integers = []
# for i in input_strings:
#     output_integers.append(int(i))
# print(output_integers," = ",sum(output_integers))

output_integers = [int(num) for num in input_strings if len(num) < 3]
# print(output_integers," = ",sum(output_integers))

#--------------- Set Comprehensions --------------------
Book = namedtuple("Book",["author","title","genre"])

books = [Book("Pratchett", "Nightwatch", "fantasy"),
         Book("Pratchett", "Thief Of Time", "fantasy"),
         Book("Le Guin", "The Dispossessed", "scifi"),
         Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
         Book("Turner", "The Thief", "fantasy"),
         Book("Phillips", "Preston Diamond", "western"),
         Book("Phillips", "Twice Upon A Time", "scifi"),
         ]

fantasy_authors = {b.author for b in books if b.genre == "fantasy"}
# print(fantasy_authors)

# --------- Dictionary  Comprehensions ---------------

fantasy_titles = {b.title : b for b in books if b.genre == "fantasy"}
# print(fantasy_titles)

#------- Generator Expressions--------
# inname = sys.argv[1]
# outname = sys.argv[2]

# with open(inname) as infile:
#     with open(outname,"w") as outfile:
#         warnings = (line for line in infile if "WARNING" in line)
#         for l in warnings:
#             outfile.write(l)

# -------- Generators ---------------------
# with open(inname) as infile:
#     with open(outname,"w") as outfile:
#         warnings = (l.replace("WARNING","") for l in infile if "WARNING" in l) 
#         for l in warnings:
#             outfile.write(l)


#---Generator Class
class WarningFilter:
    def __init__(self,sequence):
        self.sequence = sequence

    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.sequence.readline()
        while line and "WARNING" not in line:
            line = self.sequence.readline()
        if not line:
            raise StopIteration()
        return line.replace("WARNING","")
    
# ---True Generator
def warnings_filter(insequence):
    for line in insequence:
        if "WARNING" in line:
            yield line.replace("WARNING" ,"")

# with open(inname) as infile:
#     with open(outname,"w") as outfile:
#         filter = warnings_filter(infile)
#         for line in filter:
#             outfile.write(line)
            
def warnings_filter2(filename):
    with open(filename) as infile:
        yield from (line.replace("WARNING","") for line in infile if "WARNING" in line)

# filter = warnings_filter2(inname)
# with open(outname,"w") as outfile:
#     for line in filter:
#         outfile.write(line)
        
# ----- Walking a general tree problem -----------------
        
class File:
    def __init__(self,name):
        self.name = name

class Folder(File):
    def __init__(self,name):
        super().__init__(name)
        self.childern = []

root = Folder("")
etc = Folder("etc")
root.childern.append(etc)
etc.childern.append(File("passwd"))
etc.childern.append(File("groups"))
httpd = Folder("httpd")
etc.childern.append(httpd)
httpd.childern.append(File("http.conf"))
var = Folder("var")
root.childern.append(var)
log = Folder("log")
var.childern.append(log)
log.childern.append(File("message"))
log.childern.append(File("kernel"))

def walk(file):
    if isinstance(file,Folder):
        yield file.name + "/"
        for f in file.childern:
            yield from walk(f)
    else:
        yield file.name

for i in walk(root):
    print(i)