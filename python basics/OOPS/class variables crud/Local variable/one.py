class Test:
    a=100  #static
    def m1(self):
        self.b=200 #instance variable
        c=300        #local variable(local scope or function scope)
        print(c)

t1=Test()
t1.m1()        