def verify(func):
    def inner(name):
        if name=="Modi":
            print("Modi prime minister of india")
        else:
             func(name) 
    return inner       



@verify
def employee(name):
    print("Hai",name)


employee("Modi")
employee("sunil")    