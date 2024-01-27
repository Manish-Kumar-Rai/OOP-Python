#------------ Python Object Oriente Shortcuts -----------------
import sys
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
    
filename = sys.argv[1]

for index,line in enumerate(filename):
    print(f"{index+1}: {line}\n",end="")
