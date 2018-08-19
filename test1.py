class people:
    name = ""
    age = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printInfo(self):
        print("myName is",self.name)
        print("myAge is",self.age)
#   继承
class student(people):
    grade = 0;

    def __init__(self,name,age,grade):
        people.__init__(self,name,age)
        self.grade = grade
    def printInfo(self):
        print("myName is", self.name)
        print("myAge is", self.age)
        print("myGrade is", self.grade)

x = student("zhangsan",12,3)
x.printInfo()
