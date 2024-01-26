#--------------------- Python Data Structures --------------------

# all import
import datetime
from collections import namedtuple
from collections import defaultdict
from collections import Counter
from dataclasses import make_dataclass
from dataclasses import dataclass
from typing import Any
from pprint import pprint
import string
from functools import total_ordering
from operator import itemgetter
#--------------empty objects----------------
o = object()
# o.x = 5  not possible

# empty object class of our own
class MyObject:
    pass

m = MyObject()
m.x = "attribute"
# print(m.x)

#------------ Tuples and named tuples------------------
stock = "FB", 177.49, 178.88, 175.60
stock1 = ("FB", 177.49, 178.88, 175.60)
# print(type(stock),type(stock1))

def middle(stock,date):
    _, _, high, low = stock
    return ((high + low) / 2, date) 

mid_value, date = middle(stock, datetime.date(2024,1,18))
# print(mid_value, date)

Stock = namedtuple("MyStock",["symbol","current","high","low"])
stock = Stock("FB",45,high=47,low=42)
# print(stock.current)

# --------------Dataclasses -----------------
Stock = make_dataclass("MyStock",["symbol","current","high","low"])
stock1 = Stock("FB",45,high=47,low=42)
stock2 = Stock("FB",45,high=47,low=42)
#String reprensentation
# print(stock1)
#equality check
# print(stock1 == stock2)

class RegClass:
    def __init__(self,symbol,current,high,low):
        self.symbol = symbol
        self.current = current
        self.high = high
        self.low = low

regStock1 = RegClass("FB",45,high=47,low=42)
regStock2 = RegClass("FB",45,high=47,low=42)

# String representation
# print(regStock1)
#equality check
# print(regStock1 == regStock2)

@dataclass(order=True)
class StockDecorated:
    name : str
    current : float = 0.0
    high : float = 0.0
    low : Any = 0.0

stock_ordered1 = StockDecorated("FB", 177.46, high=178.67, low=175.79)
stock_ordered2 = StockDecorated("FB")
stock_ordered3 = StockDecorated("FB", 178.42, high=179.28, low=176.39)

# print(stock_ordered1 < stock_ordered2)
# print(stock_ordered1 > stock_ordered2)
# pprint(sorted([stock_ordered1, stock_ordered2, stock_ordered3]))

# pprint(stock_ordered1.__dict__)


#--------------- Dictionaries ------------------------

@dataclass
class Stock:
    current:float
    high:float
    low:float

stocks = {
    "GOOG": Stock(1235.20, 1242.54, 1231.06),
    "MSFT" : Stock(110.41, 110.45, 109.84),
}

# pprint(stocks)
# pprint(stocks["GOOG"].current)
# print(stocks.get("RIM"))
# print(stocks.get("RIM","NOT FOUND"))

# pprint(stocks.setdefault("GOOG","Invalid"))
# pprint(stocks.setdefault("RIM","This value is set to rim using setdefault method."))
stocks["GOOG"] = (1245.21, 1252.64, 1245.18)
# pprint(stocks)

def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter,0)
        frequencies[letter] = frequency + 1
    return frequencies

# pprint(letter_frequency("manishkumarrai"))

def letter_frequency2(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies

# pprint(letter_frequency2("manishkumarrai"))


class MyCounter:
    def __init__(self):
        self.num = 0
    def increment(self):
        self.num += 1
        return (self.num,[])


dict1 = defaultdict(MyCounter().increment)
dict1["a"][1].append("hello")
dict1["b"][1].append("world")
# print(dict1['b'])

dict2 = defaultdict(MyCounter().increment)
dict2["c"][1].append("Manish")
dict2["c"][1].append("Kumar")
dict2["d"][1].append("Rai")
# print(dict2)

#------------ Counter------------
def letter_frequency3(sentence):
    return Counter(sentence)

# pprint(letter_frequency3("manishkumarrai"))

responses = [
 "vanilla",
 "chocolate",
 "vanilla",
 "vanilla",
 "caramel",
 "strawberry",
 "vanilla"
]

# pprint(Counter(responses).most_common())
# pprint(Counter(responses).most_common(1)[0][0])
# pprint(Counter(responses).most_common(len(set(responses))))

#----------------- List----------------------------
def letter_frequency4(sentence):
    CHARACTERS = list(string.ascii_letters) + [" "]
    frequencies = [(c,0) for c in CHARACTERS]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter,frequencies[index][1]+1)
    return frequencies
# pprint(letter_frequency4("manishkumarrai"))

#----Sorting of list-----------
# arr = list(set("ManishKumarRai"))
# arr.sort()
# pprint(arr)

@total_ordering
class WierdSortee:
    def __init__(self,string,number,sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self,object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string
    
    def __repr__(self):
        return f"{self.string} : {self.number}"
    
    def __eq__(self,object):
        return all((
            self.string == object.string,
            self.number == object.number,
            self.sort_num == object.number, 
        ))

# a = WierdSortee("a",5,True)
# b = WierdSortee("b",6,True)
# c = WierdSortee("c",2,True)
# d = WierdSortee("d",3,True)

# l = [a,b,c,d]
# l.sort()
# pprint(l)

# for i in l:
#     i.sort_num = False

# l.sort()
# pprint(l)
    
l = ["hello", "HELP", "Helo"]
l.sort()
# pprint(l)
l.sort(key=str.lower)
# pprint(l)

l = [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]
l.sort()
# pprint(l)
l.sort(key=itemgetter(1))
# pprint(l)
