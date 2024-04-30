'''variables -nothing but container used to store data
variables are two types:
-golobal  variabl:we decalaring variable outside the function(global scope/entire file level scope)
-local variable:we are declaring variable inside the fuction(local scope or block/function level scope)
'''

min_bal=500

def account_details(id,name):
    acc_bal=50000

account_details(101,"sunil")
print(min_bal)
print(acc_bal) #cant access this is local scope/fuction level scope

