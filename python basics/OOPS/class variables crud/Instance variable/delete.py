class Account:
    def __init__(self):
        self.acc_bal=500
    def get_bal(self):
        return self.acc_bal
    def update_bal(self):
        self.acc_bal=8000
    def delete_bal(self):
        del self.acc_bal          #inside class using del keyword(del self.variable)

a1=Account()
print(a1.__dict__)   

a1.delete_bal()                   #outside a class using object (del object.variable)
print(a1.__dict__)

        