import csv 
import datetime
import os

def give_order():
    with open("Menu.txt","r") as f:
        lines = f.read()
        print(lines)
    base = input("Please choose pizza base:\n")
    while base.isdigit() == False:
        base = input("Please choose valid pizza base:\n")
    intbase = int(base)
    while 1>intbase or intbase>4:
        intbase = int(input("Please choose valid pizza base:\n"))
    sauce = input("Please choose pizza sauce:\n")
    while sauce.isdigit() == False:
        sauce = input("Please choose valid pizza sauce:\n")
    intsauce = int(sauce)
    while 11>intsauce or intsauce>16 : 
        intsauce = int(input("Please choose valid pizza sauce:\n"))
    fullPizza(intbase,intsauce)
def to_csv(sauceDescription,baseDescription,totalCost):
    sauceDescription += " "+baseDescription
    if os.path.exists("Orders_Database.csv"):
        with open("Orders_Database.csv", "a",newline="") as file:
            firstName = input("Please enter your name:\n")
            lastName = input("Please enter your surname:\n")
            id = input("Please enter your TC id:\n")
            while id.isdigit() == False:
                id = input("TC id must include 11 digits.Please enter again:\n")
            while len(id)!=11:
                id = input("TC id must include 11 digits.Please enter again:\n")
            creditCardNo = input("Please enter your credit card number:\n")
            while creditCardNo.isdigit() == False:
                creditCardNo = input("Credit card number must include 16 digits.Please enter again:\n")
            while len(creditCardNo)!=16:
                creditCardNo = input("Credit card number must include 16 digits.Please enter again:\n")
            creditCardPassword = input("Please enter your credit card password:\n")
            while creditCardPassword.isdigit() == False:
                creditCardPassword = input("Credit card password must include 4 digits.Please enter again:\n")
            while len(creditCardPassword)!=4:
                creditCardPassword = input("Credit card password must include 4 digits.Please enter again:\n")
            writer = csv.writer(file)
            writer.writerow([firstName,lastName,id,creditCardNo,creditCardPassword,sauceDescription,totalCost,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    else:        
        with open("Orders_Database.csv", "w",newline="") as file:
            firstName = input("Please enter your name:\n")
            lastName = input("Please enter your surname:\n")
            id = input("Please enter your TC id:\n")
            while id.isdigit() == False:
                id = input("TC id must include 11 digits.Please enter again:\n")
            while len(id)!=11:
                id = input("TC id must include 11 digits.Please enter again:\n")
            creditCardNo = input("Please enter your credit card number:\n")
            while creditCardNo.isdigit() == False:
                creditCardNo = input("Credit card number must include 16 digits.Please enter again:\n")
            while len(creditCardNo)!=16:
                creditCardNo = input("Credit card number must include 16 digits.Please enter again:\n")
            creditCardPassword = input("Please enter your credit card password:\n")
            while creditCardPassword.isdigit() == False:
                creditCardPassword = input("Credit card password must include 4 digits.Please enter again:\n")
            while len(creditCardPassword)!=4:
                creditCardPassword = input("Credit card password must include 4 digits.Please enter again:\n")
            writer = csv.writer(file)
            writer.writerow(["Name","Surname","TC Id","Credit Card Number","Credit Card Password","Pizza","Total Amount","Order Datetime"])
            writer.writerow([firstName,lastName,id,creditCardNo,creditCardPassword,sauceDescription,totalCost,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
class Pizza:
    def __init__(self,name,pizzaCost):
        self.name = name
        self.pizzaCost = pizzaCost
    def get_description(self):
        return self.name
    def get_cost(self):
        return self.pizzaCost

class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza", 25)
class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza", 30)
class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Turk Pizza", 35)
class PlainPizza(Pizza):
    def __init__(self):
        super().__init__("Plain Pizza", 20)

class Decorator():
    def __init__(self,sauce,sauceCost):
        self.sauce = sauce
        self.sauceCost = sauceCost
    def get_description(self):
        return self.sauce
    def get_cost(self):
        return self.sauceCost
class Olive(Decorator):
    def __init__(self):
        super().__init__("Olive", 10)
class Mushroom(Decorator):
    def __init__(self):
        super().__init__("Mushroom", 15)
class GoatCheese(Decorator):
    def __init__(self):
        super().__init__("Goat Cheese", 20)
class Meat(Decorator):
    def __init__(self):
        super().__init__("Meat", 25)
class Onion(Decorator):
    def __init__(self):
        super().__init__("Onion", 7.5)
class Corn(Decorator):
    def __init__(self):
        super().__init__("Corn", 12.5)

def fullPizza(base,sauce):
    if base == 1:
        p = ClassicPizza()
        baseDescription =  p.get_description()
        baseCost = p.get_cost()
    elif base == 2:
        p = MargheritaPizza()
        baseDescription = p.get_description()
        baseCost = p.get_cost()
    elif base == 3:
        p = TurkPizza()
        baseDescription = p.get_description()
        baseCost = p.get_cost()
    elif base == 4:
        p = PlainPizza()
        baseDescription = p.get_description()
        baseCost = p.get_cost()
    if sauce == 11:
        s = Olive()
        sauceDescription = s.get_description()
        sauceCost = s.get_cost()
    elif sauce == 12:
        s = Mushroom()
        sauceDescription = s.get_description()
        sauceCost = s.get_cost()
    elif sauce == 13:
        s = GoatCheese()
        sauceDescription = s.get_description()
        sauceCost = s.get_cost()
    elif sauce == 14:
        s = Meat()
        sauceDescription = s.get_description()
        sauceCost = s.get_cost()
    elif sauce == 15:
        s = Onion()
        sauceDescription = s.get_description()
        sauceCost = s.get_cost()
    elif sauce == 16:
        s = Corn()
        sauceDescription = s.get_description()
        sauceCost = s.get_cost()
    print(sauceDescription,baseDescription,"is ready. Total amount:",(baseCost+sauceCost),"$.")
    to_csv(sauceDescription,baseDescription,(baseCost+sauceCost))
    toContinue = input('If you want to give a new order please type "yes" or "YES":\n')
    if toContinue =="yes" or toContinue =="YES":
        give_order()
    else:
        print("Thank you. Enjoy your meal!")
give_order()