class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
    def compare(self):
        if(self.age==c2.age):
            return True
        else:
            return False

c1=Person("Indranil",23)
c2=Person("Ram",23)
c1.display()
c2.display()
compareAge=c1.compare()
if(compareAge):
    print("They are equal")
else:
    print("They are not equal")
