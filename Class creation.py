#
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def __str__(self):
        return f"{self.firstname}({self.lastname})"
    def printname(self):
        print(self.firstname,self.lastname)
p=Person('John',23)
print(p)

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
x = Student("Howard","Stark")
x.printname()


class Student1(Person):
    def __init__(self,fname,lname,adm):
        super().__init__(fname,lname)
        self.admNo = adm

x1 = Student1("Jesee","Mwai",123)
x1.printname()
print(x1.admNo)
