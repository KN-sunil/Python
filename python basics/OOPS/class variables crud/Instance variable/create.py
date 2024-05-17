





class Employee:
    def __init__(self,id,name):
        self.id=id                          #-Inside a constructor-using self variable
        self.name=name

    def set_sal(self,sal):
        self.esal=sal                       #-inside instance method-using self variable


a1=Employee(101,"rahul")
a2=Employee(102,"sonia")

print(a1.__dict__)
print(a2.__dict__)

a1.set_sal(55000)                         
a2.set_sal(65000)

print(a1.__dict__)
print(a2.__dict__)

a1.eloc="waynad"                              #-outside a class using object reference
print(a1.__dict__)