'''Decorators-decorators is a function it takes function as argument or input and returns function with modified functionalitis
'''
'''
def home_page(name,is_login):
    print("Home page")
def order_page(name,is_login):
    print("Orders page")    
def product_page(name,is_login):
    print("Product page")   

home_page("rahul",True)
order_page("sunil",False)
product_page("sonia",False)#here  irrespective of bool value it will  open all pages
'''
#by using decorators

def login_required(func):
    def inner(name,is_login):
        if is_login==False:
            print("Login required")
        else:
            return func(name,is_login)  
    return inner      

def home_page(name,is_login):
    print("Home page")
@login_required    
def order_page(name,is_login):
    print("Orders page")
def product_page(name,is_login):
    print("product page")        

home_page("rahul",True)
order_page("sunil",False)
product_page("sonia",False)