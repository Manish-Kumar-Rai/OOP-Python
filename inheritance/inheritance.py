#--------------- Basic Inheritance ---------------------
class Contactlist(list):
    def search(self,name):
        """Return all contacts that contains the search value in thier name."""
        matching_contacts = []
        print(self)
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
    
class Contact:
    all_contacts = Contactlist()

    def __init__(self,name="",email="",**kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        #class variable
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self,order):
        print(f"{order} order to {self.name}.")

class AddressHolder:
    def __init__(self,street="",city="",state="",code="",**kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        

class Friends(Contact,AddressHolder):
    def __init__(self,phone="",**kwargs):
        super().__init__(**kwargs)
        self.phone = phone

c = Contact("Manish Rai","vksrai95@gmail.com")
c = Contact("Vikas Rai","vksrai96@gmail.com")
# print(Contact.all_contacts)

# for contact in Contact.all_contacts:
#     print(contact.name,contact.email)
        
# s = Supplier("Avinash Rai","avirai.rai92@gmail.com")
# s.order("Electrical things")

# print([c.name for c in Contact.all_contacts.search("Rai")])

class LongDictName(dict):
    def longest_key(self):
        longest = None
        for key in self:
            print(self)
            if not longest or len(key) > len(longest):
                longest = key
        for key in self:
            print(f"value of {key} = {self[key]}")
        return longest
    
# d = LongDictName()
# d["hello"] = 1
# d["longest"] = 2
# d["Manish"] = 3

# print(d)
# print(d.longest_key())
    
#-------------------- Multiple Inheritance -------------------
class Shape:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

#--Mixin--
class Serialization:
    def serial(self):
        for k in self.__dict__:
            print(f"{k} = {self.__dict__[k]},",end=" ")
        print()
        

class Rectangle(Shape,Serialization):
    def __init__(self,x,y,height,width):
        super().__init__(x,y)
        self.height = height
        self.width = width

class Circle(Shape,Serialization):
    def __init__(self, x, y,radius):
        super().__init__(x, y)
        self.radius = radius

# rectangle = Rectangle(0,0,100,200)
# rectangle.serial()

# circle = Circle(0,0,40)
# circle.serial()
        

# ------------- The Diamond Problem -----------------------
# Base class should only be called once.
class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method of BaseClass.")
        self.num_base_calls += 1

class LeftSubClass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method of Left Subclass.")
        self.num_left_calls += 1

class RightSubClass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method of Right Subclass.")
        self.num_right_calls += 1

class Subclass(LeftSubClass,RightSubClass):
    num_subclass_calls = 0 
    def call_me(self):
        super().call_me()
        print("Calling method of Subclass.")
        self.num_subclass_calls += 1

# subclass = Subclass()
# subclass.call_me()
# print(subclass.num_subclass_calls,
#       subclass.num_left_calls,
#       subclass.num_right_calls,
#       subclass.num_base_calls)
        
# ------- Polymorphisms --------------------------
class AudioFile:
    def __init__(self,filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid File Format !")
        self.filename = filename

class Mp3File(AudioFile):
    ext = "mp3"

    def play(self):
        print(f"Playing {self.filename} as mp3 file.")

class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print(f"Playing {self.filename} as wav file.")

# mp3file = Mp3File("manish.mp3")
# mp3file.play()

# wavfile = WavFile("vikas.wav")
# wavfile.play()
        

##----- Duck Typing
class FlacFile:
    def __init__(self,filename):
        if not filename.endswith(".flac"):
            raise Exception('Invalid File Format !')
        self.filename = filename

    def play(self):
        print(f"Playing {self.filename} as flac file.")

flacfile = FlacFile("Avinash.flac")
flacfile.play()


#------------------- Abstract Base Class--------------------------------
from collections.abc import Container

class OddContainer:
    def __contains__(self,x):
        if not isinstance(x,int) or x % 2:
            return True
        return False
    
odd_container = OddContainer()
# print(isinstance(odd_container,Container))
# print(issubclass(OddContainer,Container))
# print(1 in odd_container)
# print(2 in odd_container)
# print(3 in odd_container)


import abc

class MediaLoader(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls,C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented
        