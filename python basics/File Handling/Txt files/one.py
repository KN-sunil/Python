#reading user.txt file and printing data
fp=open("user.txt","r")
data=fp.read()

print(data)
print(type(fp))
fp.close()