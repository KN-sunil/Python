"""
1.Inside a class outside any method
2.inside constructor method also possible but using class name
3.inside instance method using class name
4.inside class method using class name
5.inside static method using class name"""

class Account:
    min_bal=500             #1
    def __init__(self,id):
        self.acc_id=id
        Account.branchname="marathahalli"  #2
    def set_branchid(self):
       Account.set_branchid=655  #3

    @classmethod  
    def updateparent_branch(cls):
        cls.parentbranch="banglore" #4

    @staticmethod
    def tax_cal():
        Account.tax=11     #5


a1=Account(101)
a2=Account(102)
print(Account.__dict__)   

a1.set_branchid()
a1.updateparent_branch()
a1.tax_cal()
print(Account.__dict__)