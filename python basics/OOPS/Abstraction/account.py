from bank import Bank

class Account(Bank):
    def cal_bal(self):
        print("Account class-cal_bal method")

a1=Account()
a1.cal_bal()        