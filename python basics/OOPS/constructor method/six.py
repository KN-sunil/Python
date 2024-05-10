class Account:
    min_bal=500
     
    def __init__(self,id,name,email,amount):
          self.acc_id=id
          self.acc_name=name
          self.acc_email=email
          self.acc_bal=amount
        
    def open_accout(self):
        print("account opened succefully")

    def deposit_ampount(self,amount):
        print("amount deposited succefully")   


a1=Account('101','sunil','sunil@gmail.com',5000)   
a2=Account('102','jaivik','jaivik@gmail.com',10000)  
a3=Account('103','bablu','bablu@gmail.com',15000)     

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
print(Account.__dict__)