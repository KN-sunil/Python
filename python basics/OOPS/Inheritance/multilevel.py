class GP:
    def m1(self):
        print("grandparent class m1 method")

    def m2(self):
        print("grandparent class m2 method")

class Parent(GP):
    def m3(self):
        print("parent class m3 method")    

    def m4(self):
        print("parent class m4 method")

class Child(Parent):
    def m5(self):
        print("child class m5 method") 

c1=Child()
c1.m1()
c1.m2()
c1.m3()
c1.m4()
c1.m5()                           