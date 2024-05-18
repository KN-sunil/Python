"""
how to achive abstraction:
by using a module called abc that contains class members
*ABC(base class)
*@abstractmethod(decorator)

note:
suppose you are creating class as abstract class you cant create a class
         or
when any class is extending ABC class and class has abstract method then we cant create a object

when to use abstraction:
if you dont wnt to create object go with abstraction
"""

from abc import *

class Account(ABC):         #here we cant create object becz account class is extending ABC and has abstract method

    @abstractmethod
    def cal_bal(self):
        pass

Account()    




from abc import *

class Account:         #here we can create object becz account class is not extending ABC and has abstract method

    @abstractmethod
    def cal_bal(self):
        pass

a1=Account()
print(a1)
print(id(a1))    