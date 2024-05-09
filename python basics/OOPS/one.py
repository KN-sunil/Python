class Account:
    def open_acc(self):                      #self is pointer pointing to current object used to acces the members inside classs  #for outside of the class we object
        print("account opened")
    def deposit_amount(self):
        print("amount deposited")
    def withdrawl(self):
        print("amount withdrawl")
    def get_bal(self):
        print('balance')

a1=Account()
a1.open_acc()
a1.deposit_amount()
a1.withdrawl()
a1.get_bal()