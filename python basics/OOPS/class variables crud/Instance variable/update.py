class Account:
    def __init__(self):
        self.acc_bal=5000

    def get_bal(self):
        return self.acc_bal

    def update_bal(self):
        self.acc_bal=82000        #inside class using self 

a1=Account() 
print(a1.get_bal())
print(a1.acc_bal)

a1.update_bal()                   #outside class using object

print(a1.get_bal())
print(a1.acc_bal)
        