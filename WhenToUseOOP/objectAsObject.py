#---------------When to use object as Object ----------------------------
import math
#----perimeter of a polygon  (Function based)-------------
square = [(1,1),(1,2),(2,2),(2,1)]

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    for i in range(len(polygon)):
        perimeter += distance(points[i],points[i+1])
    return perimeter

# print(perimeter(square))

#----perimeter of a polygon  (OOP based)-------------

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)
    
class Polygon:
    def __init__(self):
        self.vertices = []

    def add_points(self,polygon):
        for i in range(len(polygon)):
            self.vertices.append((Point(polygon[i][0],polygon[i][1])))

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter
    
class ModifiedPolygon(Polygon):
    def __init__(self,points):
        super().__init__()
        points = points if points else []
        for point in points:
            if isinstance(point,tuple):
                point = Point(*point)
            self.vertices.append(point)

    def perimeter(self):
        return super().perimeter()
    
modifiedpolygon = ModifiedPolygon(square)
# print(modifiedpolygon.perimeter())

class Color:
    def __init__(self,rgb_value,name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self,name):
        if not name:
            raise Exception("Invalid name!")
        self._name = name

    def _get_name(self):
        return self._name
    
    name = property(_get_name,_set_name)
    

# color = Color("#ff0000","bright red")
# print(color.name)
# color.name = "red"
# color.name = "blue"
# print(color.name)
    
# class Silly:
#     def _set_silly(self,value):
#         print(f"You are making silly {value}.")
#         self._silly = value

#     def _get_silly(self):
#         """This are silly properties"""
#         print("You are getting silly.")
#         return self._silly
    
#     def _del_silly(self):
#         print("Whoa! You are deleting silly.")
#         del self._silly

#     silly = property(_get_silly,_set_silly,_del_silly,)

# print(help(Silly))
    
class Foo:
    @property
    def foo(self):
        return self._foo
    
    @foo.setter
    def foo(self,value):
        self._foo = value

 
# f = Foo()
# f.foo = "manish"
# print(f.foo)
        
class Silly:
    @property
    def silly(self):
        """This is silly properties."""
        print("You are getting silly.")
        return self._silly
    
    @silly.setter
    def silly(self,value):
        print("You are setting silly.")
        self._silly = value

    @silly.deleter
    def silly(self):
        print("Whoa! You are deleting silly.")
        del self._silly

# s = Silly()
# s.silly = "funny"
# print(s.silly)
# del s.silly
        
from urllib.request import urlopen

class WebPage:
    def __init__(self,url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Webpage...")
            self._content = urlopen(self.url).read()
        return self._content

# import time
# webpage = WebPage("http://ccphillips.net/")
# t1 = time.time()
# content1 = webpage.content
# t2 = time.time()
# print(f"First: {round(t2-t1,4)}")
# t3 = time.time()
# content2 = webpage.content
# t4 = time.time()
# print(f"Second: {round(t4-t3,4)}")
    
# class Average(list):
#     @property
#     def average(self):
#         return sum(self) / len(self)
    
# a = Average([4,7,8,945,56,78])
# print(a.average)
    

#------------Manager Objects------------------
import shutil
import sys
import zipfile
from pathlib import Path

class ZipReplace:
    def __init__(self,filename,search_string,replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path(f"unzipped_{filename}")

    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        print(self.filename)
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(self.temp_directory)

    def find_replace(self):
        for filename in self.temp_directory.iterdir():
            with open(filename) as file:
                contents = file.read()
            contents = contents.replace(self.search_string,self.replace_string)
            with open(filename,"w") as file:
                file.write(contents)


    def zip_files(self):
        with zipfile.ZipFile(self.filename, "w") as file:
            for filename in self.temp_directory.iterdir():
                file.write(filename, filename.name)
        shutil.rmtree(self.temp_directory)


if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).zip_find_replace()