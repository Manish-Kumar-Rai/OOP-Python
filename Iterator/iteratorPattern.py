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
print(fantasy_titles)


