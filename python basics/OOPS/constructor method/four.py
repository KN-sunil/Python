class Account:
    def open_account(self):
        print("account opened successfully!")
    def deposit_amount(self,amount):
        print("amount deposited successfully")

a1 = Account(101,'Rahul','rahul@gmail.com')

#this gives error at the time of object creation we are passing object values 
#to receive object values definitly we need one special constructor method