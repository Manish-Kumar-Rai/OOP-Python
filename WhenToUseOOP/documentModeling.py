#  Modeling a Document class that might be used in a text editor or word processor.

class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ""

    def insert(self,character):
        if not hasattr(character,"character"):
            character = Character(character)
        self.characters.insert(self.cursor.position,character)
        self.cursor.position += 1

    def delete(self):
        del self.characters[self.cursor.position]

    def save(self):
        with open(self.filename,"w") as file:
            file.write("".join((str(c) for c in self.characters)))

    @property
    def contents(self):
        return "".join((str(c) for c in self.characters))


class Cursor:
    def __init__(self,document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def backward(self):
        self.position -= 1

    def home(self):
        while self.document.characters[self.position - 1].character != "\n":
            self.position -= 1
            if self.position == 0:
                #Got to beginning of file befor newline
                break
    
    def end(self):
        while (
            self.position < len(self.document.characters)
            and self.document.characters[self.position].character != "\n"
        ):
            self.position += 1

"""
Whenever we print the string, each bold character is preceded by a (*) character, each italicized character by a (/) character, and each underlined character by a (_) character.

Naturally, we'd want to display real bold, italic, and underlined fonts in a UI, instead of using our __str__ method, but it was sufficient for the basic testing we demanded of it.
"""

class Character:
    def __init__(self,character,bold=False,italic=False,underline=False):
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline


    def __str__(self):
        bold = "*" if self.bold else ""
        italic = "/" if self.italic else ""
        underline = "_" if self.underline else ""
        return bold + italic + underline + self.character

doc = Document()
doc.filename = "test_document"
doc.insert('h')
doc.insert('e')
doc.insert(Character('l', bold=True))
doc.insert(Character('l', bold=True))
doc.insert('o')
doc.insert('\n')
doc.insert(Character('w', italic=True))
doc.insert(Character('o', italic=True))
doc.insert(Character('r', underline=True))
doc.insert('l')
doc.insert('d')
print(doc.contents)

doc.cursor.home()
doc.delete()
doc.insert('W')
print(doc.contents)

doc.characters[0].underline = True
print(doc.contents)
doc.save()
