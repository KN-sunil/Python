import csv
fp=open("data.csv","r")
user_data=csv.reader(fp)
users=list(user_data)

for user in users:
    for data in user:
        print(data)
    
fp.close()