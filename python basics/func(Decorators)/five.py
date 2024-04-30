def user_uppercase(func):
    def inner():
        msg=func()
        return msg.upper()
    return inner

@user_uppercase
def wish_user():
    return "Hi Sunil"
print(wish_user())