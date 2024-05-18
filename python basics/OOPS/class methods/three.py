"""
Class method:
to access the class variables we use class method
we can declare class method using class method decorator(@classmethod)
if we are using class/static variable go with class method
here we no need to create object without creating object we are accessing the class

when to use:
if you want do operation without creating object go with class method
"""
class Account:
    min_bal=500

    @classmethod
    def get_min_bal(cls):
        return cls.min_bal

print(Account.get_min_bal())       
