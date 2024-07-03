class myclass:
    x=10
obj = myclass()
print(obj.x)

class myclass2 :
    def __init__(self,name,rollno) :
         self.name=name
         self.rollno = rollno
p1 = myclass2("hello","hi")
print(p1.name)