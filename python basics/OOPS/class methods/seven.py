"""
Static mthod:
to define/create general utility methods we are going to use static method
here there is no argument like self and cls
here also no need to create obejct,without creating objects only we can access the class
"""

class Account:

    @staticmethod
    def cal_tax(p,r,t):
        return p*r*t/100
    

print(Account.cal_tax(100000,1,1))    