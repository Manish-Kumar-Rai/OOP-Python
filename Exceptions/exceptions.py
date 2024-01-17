#--------------------------- Exceptions --------------------------
class Evenonly(list):
    def append(self,integer):
        if not isinstance(integer,int):
            raise TypeError("Only integer can be added.")
        if integer % 2:
            raise ValueError("Only even number can be added.")
        super().append(integer)

def no_return():
    print("I will raise an Exceptions.")
    raise Exception("This is always raised.")
    print("This line will never execute.")
    return "I won't be returned."

def call_exceptor():
    print("call exceptor starts here.")
    no_return()
    print("an exceptions was raised...")
    print("...so this line don't run.")

# try:
#     no_return()
# except:
#     print("I caught an exceptions.")
#     print("executed after the exception.")
    
# def funny_divisor(divider):
#     try:
#         if divider == 13:
#             raise ValueError("13 is unlucky number.")
#         return 100 / divider
#     except ZeroDivisionError:
#         return "Enter the number other than Zero."
#     except TypeError:
#         return "Enter a numerical value."
#     except ValueError:
#         print("no,no,Not 13!!!")
#         # raise
    
# print(funny_divisor(0))
# print(funny_divisor("Manish"))
# print(funny_divisor(13))
    
# try:
#     raise ValueError("This is an argument.")
# except ValueError as e:
#     print("the exception arguments were: ", e.args)
    
# import random

# some_exceptions = [ValueError,TypeError,IndexError,None]

# try:
#     choice = random.choice(some_exceptions)
#     if choice:
#         raise choice
# except ValueError:
#     print("Caught Value Error.")
# except TypeError:
#     print("Caught Type Error.")
# except Exception as e:
#     print(f"Caught some other error: {e.__class__.__name__}")
# else:
#     print("This code called if no exceptions is raised.")
# finally:
#     print("this clean up code will always run.")
    

def dummy():
    try:
        return "First"
    except:
        pass
    finally:
        print("Second")

# print(dummy())

# balance = 167

# class InvalidWithdrawal(Exception):
#     def __init__(self,amt,balance):
#         super().__init__(f"You don't have {amt} amount.")
#         self.amt = amt
#         self.balance = balance

#     def overage(self):
#         overage = self.amt - self.balance
#         print(f"Your enter amount: {self.amt}\nBut your available balance is: {self.balance}\nyou lack {abs(overage)} rupee in your current balance.")

# amt = int(input("Enter amount to withdraw: "))
# try:
#     if amt > balance:
#         raise InvalidWithdrawal(amt,balance)
# except InvalidWithdrawal as e:
#     print(e.args[0])
#     e.overage()


def divide_with_exception(number,divisor):
    try:
        print(f"{number} / {divisor} = {number/divisor}")
    except ZeroDivisionError:
        print("You can't divide a number by Zero.")

def divide_with_if(number,divisor):
    if divisor == 0:
        print("You can't divide a number by Zero.")
    else:
        print(f"{number} / {divisor} = {number/divisor}")

divide_with_exception(25,5)
divide_with_if(36,6)
divide_with_if(36,0)