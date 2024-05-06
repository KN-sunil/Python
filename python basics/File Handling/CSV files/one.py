# CSV FILE:defines data in the form of comma separate version
# how to handle:using inbuilt csv module

# csv module members:
# -writer()
# -reader()
# -writers()

#read csv file and print data
import csv
fp=open("data.csv","r")
user_data=csv.reader(fp)
users=list(user_data)
print(users)

fp.close()