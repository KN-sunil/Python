class Account:
    def __init__(self):
        self.acc_bal=5000       #inside class using self

    def get_bal(self):
        return self.acc_bal


a1=Account()
print(a1.get_bal())
print(a1.acc_bal)             #outside a class using object
