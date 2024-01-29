#------------ Python Object Oriente Shortcuts -----------------
import sys
import random,string
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

print(joiner.result)