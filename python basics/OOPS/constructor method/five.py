class Account:
    
    def __init__(self,id,name,email):
        self.acc_id=id
        self.acc_name=name
        self.acc_email=email
        
    def open_account(self):
        print("account opened successfully!")
    def deposit_amount(self,amount):
        print("amount deposited successfully")

a1 = Account(101,'sunil','sunil@gmail.com')
a2 = Account(102,'jaivik','jaivik@gmail.com')
a3 = Account(103,'bablu','bablu@gmail.com')


print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)