#program to find number of objcts created in class

class Account:
    noobject=0

    def __init__(self):
        Account.noobject= Account.noobject+1

a1=Account()  
a1=Account()        
a1=Account()  
a1=Account()  
a1=Account()  
print(Account.noobject)
