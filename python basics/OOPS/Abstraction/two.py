class Account:

    @abstractmethod         #here i dont know the implemantation so dclaring as abstract method
    def cal_bal(self):
        pass

    class SA(Account):    #child class is responsible for implementation of cal_bal,then only child class is going to create object and access method
        pass
