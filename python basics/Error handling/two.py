fp=None
try:
    fp=open("xyz.txt","r")

except:
    fp=open("abc.txt","r")

data=fp.read()
print(data) 
fp.close()       
