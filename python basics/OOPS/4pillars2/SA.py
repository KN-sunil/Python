from Account import Account


class SA(Account):
    min_bal=500
    def __init__(self,id,name,email,address,amount):
        super().__init__(name,email,address)
        self.acc_id=id
        self.acc_bal=amount

    def cal_bal(self):
        return self.acc_bal-self.min_bal



# sa1=SA(101,"rahul","rahul@gmail.com","banglore",6000)
# print(sa1.__dict__)
# print(sa1.cal_bal())
# sa1.set_mobile_no(9739129213)
# print(sa1.get_mobile_no())
# print(sa1.__dict__)