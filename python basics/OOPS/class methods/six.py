#program to find number of objcts created in class 

class Account:
    noobject=0

    def __init__(self):
        Account.noobject= Account.noobject+1
    
    @classmethod
    def get_noobject(cls):            #another way using class method
        return cls.noobject
                          

a1=Account()  
a1=Account()        
a1=Account()  
a1=Account()  
a1=Account()  
print(Account.noobject)
print(Account.get_noobject())
