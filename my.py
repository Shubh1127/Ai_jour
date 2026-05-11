class BankAccount:
        def __init__(self,account_number,owner_name,balance):
                    self.owner_name=owner_name
                    self.__balance=balance
                    self.__account_number=account_number
        
        def get_balance(self):
                    return self.__balance
    
        def get_account(self):
                    return self.__account_number
        def deposit(self,amount):
                    if amount>0:
                                self.__balance+=amount
                                print("amount is depositied")
                                print(f"updated balance is: {self.get_balance()}")
                    else:
                                print("Enter valid amount")
        def withdraw(self,amount):
                    if self.__balance >0 and self.__balance >amount:
                                self.__balance -= amount
                                print(f"{amount} is withdrawl")
                                print(f"updated balance is: {self.get_balance()}")
                    else:
                            print("not Enough balance or amount is invalid")

acc1=BankAccount(123,"shubham",5000)

print(acc1.get_account())
print(acc1.owner_name)
print(acc1.get_balance())
acc1.deposit(1000)
acc1.withdraw(500)

class Book:
        def __init__(self,title,author,reviews):
                    self.title=title
                    self.author=author
                    self.reviews=reviews
        
        def add_review(self,review):
                    self.reviews.append(review)
                    print(f"{review} is added\n\n ")
                    
                    for r in self.reviews:
                            print(r)
        def count_reviews(self):
                return len(self.reviews)
        
        def display_reviews(self):
                    for r in self.reviews:
                            print(r,"\t")

b=Book("python","shubh",["Nice","Good","great","excellent"])

print(f"Title: {b.title}")
print(f"Author: {b.author}")
print(f"Number of reviews: {b.count_reviews()}")
b.display_reviews()
b.add_review("awesome")

class Student:
        def __init__(self,name,roll_no,marks):
                    self.__name=name
                    self.__roll_no=roll_no
                    self.__marks=marks

        def get_info(self):
                if self.__name or self.__marks or self.__roll_no:
                                return self.__name,self.__marks,self.__roll_no
        def set_name(self,name):
                if isinstance(name,str):
                        self.__name=name
                        print(f"name  is updated\n now name is: {self.__name}")
                else:
                        print("name type is invalid")    
        def set_marks(self,marks):
                    if isinstance(marks,int):
                                if marks>=0:
                                            self.__marks=marks
                                            print(f"marks is updated\n updated marks are: {self.__marks}")
                                else:
                                        print("marks cannot be in negative")
                    else:
                            print("marks type is wrong\n better to enter an integer")
        def set_roll(self,roll):
                    if isinstance(roll,int):
                                if roll>0 and roll<=100:
                                        self.__roll_no=roll
                                        print(f"roll no is updated\n your roll no is: {self.__roll_no}")
                                else:
                                        print("roll no can't be in negative")
                    else:
                            print("roll no type is wrong]n better to enter an integer")
            

s=Student("shubham",75,99)

print(s.get_info())

s.set_name("shubh")
s.set_marks(-95)
s.set_roll(-21)


class Shape:
        def area(self):
                pass
class Circle(Shape):
        def area(self,radius):
                return 3.14*radius*radius
class Rectangle(Shape):
        def area(self,length,breadth):
                return length*breadth
class Triangle(Shape):
        def area(self,base,height):
                return 0.5*base*height
c=Circle()
print(f"area of circle is: {c.area(5)}")   
r=Rectangle()
print(f"area of rectangle is: {r.area(4,6)}")   
t=Triangle()
print(f"area of triangle is: {t.area(4,6)}")

class Vehicle:
        def __init__(self,brand,model):
                self.brand=brand
                self.model=model
        
class Car(Vehicle):
        def __init__(self,seat,brand,model):
                super().__init__(brand,model)
                self.seat=seat
class Bike(Vehicle):
        def __init__(self,engine_cc,brand,model):
                self.engine_cc=engine_cc
                super().__init__(brand,model)

f=open("sample.txt","a")
f.write("This is a sample text file.\n")
f.close()
f.open("sample.txt","r")
print(f.read())

with open("sample.txt","r") as f:
        print(f.read())

data=True
line=0
with open("sample.txt","r") as f:
        while data:
                data=f.readline()
                line+=1
                if("Python" in data):
                            print("found")
                            print(line)
                            break
                print(data)

try:
    val=input("Enter the number: ")
    x=int(val)
    res=10/x
except ZeroDivisionError:
        print("You can't divide a number by zero")
except ValueError:
        print(f"You can't enter a string into a int input\n {val} invalid no.")
else:
    print(f"Divison of 10 by {x} is {res}")
finally:
        print("All code executed")

list=[-2,-4,-10,2,6,8,99]
print([0 if val <0 else val for val in list])

import json

d={
        "name": "shubham",
        "age":25,
        "isTeacher": False

}

with open("data.json","w" ) as f:
        data=json.dumps(d)
        print(type(data))

names=["shubham","harsh","dushyant","sarthak","rohan"]

with open("log.txt","a") as f:
            
            f.write("codes run successfully")

with open("log.txt","r")as t:
            data=t.read()
            print(data)

list=[5,10,15,20,25,30,40,50]

print([val for val in list if val>15])
import json
cities={
    "Delhi":"3cr",
    "gurgaon":"10L",
    "jhajjar":"50k"
}
with open("cities.json","w") as f:
            json.dump(cities,f,indent=4)

with open("cities.json","r") as t:
            data=json.load(t)

print(data)

city=input("Enter the city name: ")
pop=int(input("\nEnter the population: "))

data[city]=pop
with open("cities.json","w") as i:
        json.dump(data,i,indent=4)
        
with open("cities.json","r") as s:
            data=json.load(s)

print(data)

try:
    with open("data.txt","r") as f:
        data=f.read()
except FileNotFoundError:
        print("File not found")
else:
        print(data)