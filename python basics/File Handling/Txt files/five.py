#a-append text into emp.txt file

fp=open("emp.txt","a")
data="good night banglore"
fp.write(data)
fp.close()