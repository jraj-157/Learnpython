# 1
class programmer():
    Company_Name ="Microsoft"
    language = "C++"
    def __init__(self,name,language):
        self.name = name
        self.language = language
    def getDetalis(self):
        print(f"{self.name} works in {self.language}")
jraj157 = programmer("jraj","python")
dhoni7 = programmer("MSD","C++")

jraj157.getDetalis()
dhoni7.getDetalis()
# 2 calculator usning oops
from cmath import sqrt
class calculator():
    def __init__(self,number):
        self.number = number
        
    def ans_sqt(self):
        a = sqrt(self.number)

        print(a)
    def ans_cub(self):
        b = (self.number) *(self.number) * (self.number)
        print(b)
    def ans_square(self):
        c = (self.number) * (self.number)
        print(c)
z = int(input("Enter integer:"))
integer = calculator(z)
integer.ans_sqt()
integer.ans_cub()
integer.ans_square()
# 3
class test():
    a = 5
a = 0
print(a)
# 4
from cmath import sqrt
class calculator():
    def __init__(self,number):
        self.number = number
        
    def ans_sqt(self):
        a = sqrt(self.number)

        print(a)
    def ans_cub(self):
        b = (self.number) *(self.number) * (self.number)
        print(b)
    def ans_square(self):
        c = (self.number) * (self.number)
        print(c)
    @staticmethod
    def greet():
        print("NO CHANCE IN HELL")
z = int(input("Enter integer:"))
integer = calculator(z)
integer.ans_sqt()
integer.ans_cub()
integer.ans_square()
integer.greet()
# 5
class train():
    def __init__(self,name,fare,seats):
        self.name =name
        self.fare = fare
        self.seats = seats
    def setstatus(self):
        print(f"The seat available  {self.seats}")
        print(f"The fare {self.fare}")
        print(f"The name {self.name}")
    def booktrin(self):
        if(self.seats > 0):
            print("confiremed")
            self.seats = self.seats - 1
        else:
            print("sorry you are late")
raj0095 = train("rajdhani",150,2)
raj0095.setstatus()
raj0095.booktrin()








    








     


    
 





