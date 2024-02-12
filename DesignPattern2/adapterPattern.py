#------------------- Design Pattern 2 ------------------------

import datetime

class AgeCalculator:
    def __init__(self,birthday):
        self.year, self.month, self.day = (int(i) for i in birthday.split("-"))

    def calculateAge(self,date):
        year, month, day = (int(i) for i in date.split("-"))
        age = year - self.year
        if (month, day) < (self.month,self.day):
            age -= 1
        return age
    
# a = AgeCalculator("1998-02-25")
# print(a.calculateAge("2024-02-26"))
    
class DateAgeAdaptor:
    def _str_date(self,date):
        return date.strftime("%Y-%m-%d")
    
    def __init__(self,birthday):
        self.birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(self.birthday)

    def get_age(self,date):
        self.date = self._str_date(date)
        return self.calculator.calculateAge(self.date)
    
# adaptor = DateAgeAdaptor(datetime.datetime(1998,2,25))
# print(adaptor.get_age(datetime.datetime(2024,2,26)))

#--------Using Inheritence

class AgeableDate(datetime.date):
    def split(self,char):
        return self.year, self.month, self.day
    
# bd = AgeableDate(1998,2,25)
# a = AgeCalculator(bd)
# today = AgeableDate.today()
# print(a.calculateAge(today))