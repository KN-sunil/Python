"""
Encapsulation:
binding data and method as a one unit
how to achive:
by using instance method(setters,and getters)
"""

class Employee:
    org_name='tcs'

    def set_id(self,id):
        self.eid=id

    def get_id(self):
        return self.eid
    
e1=Employee()
e1.set_id(101)
print(e1.get_id())    