class p1:
    def m1(self):
        print("p1-m1 method")
class p2:
    def m1(self):
        print("p2-m1 method")   

class Child(p2,p1):  #if parent class has same methods it will take left to right  (MRO-METHOD RESOLUTION ORDER BASED ON EXTENDING ORDER)
    def m2(self):
        print("child -m2 method")


c1=Child()
c1.m1()
c1.m2()