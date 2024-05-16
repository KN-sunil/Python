class Parent():
    def m1(self):
        print("parent class m1 method")    


class Child1(Parent):
    def m2(self):
        print("child1 class m2 method")    

class Child2(Parent):
    def m3(self):
        print("child1 class m2 method")    


c1=Child1()
c1.m1()
c1.m2()  
# c1.m3()   this gives error bcz child1 has no relation with child 2           

c2=Child2()
c2.m1()
c2.m3() 
# c2.m2()   this gives error bcz child1 has no relation with child 2 