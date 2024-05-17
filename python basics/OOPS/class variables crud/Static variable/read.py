"""
1.inside instance method using class name,self
2.inside a constructor using classname,self
3.inside class method using cls and class name
4.inside static method using class name
5.outside a class using class name,object
"""
#5
# class Test:
#     a=100

# a1=Test()
# print(Test.a)    
# print(a1.a)

#1
# class Test:
#     a=100
#     def m1(self):
#         print(Test.a)
#         print(self.a)    

# t1=Test()
# t1.m1()  

#3
# class Test:
#     a=100
#     def m2(cls):
#         print(Test.a)
#         print(cls.a)
# t1=Test()
# t1.m2()      

#2
# class Test:
#     a=100
#     def __init__(self):
#         print(Test.a)
#         print(self.a)
# t1=Test()
        
#4
# class Test:
#     a=100
#     @staticmethod
#     def m3():
#         print(Test.a)    

# t1=Test()
# t1.m3()           
        
