#how to access local variable as gloabl variable-using global keyword

a=10
def f1():
    global b
    b=20 # acts as global variable 
f1()
print(a)
print(b)    