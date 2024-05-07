'''
Error handling:in error handling to types are there
-runtime error:one time error program terminates abnormally
-system error:
"Error handling can be achevied by try,except,finally"
try:risky code should be try block
except:alternative code should in except block
finally:mandatory code should be in finally block


'''
fp=open("xyz.txt","r")  #risky code bcz it gives file not found error
data=fp.read()
print(data)
print("reading file successfully")

fp.close()