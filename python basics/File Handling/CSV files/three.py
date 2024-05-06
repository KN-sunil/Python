import csv
fp=open("data.csv","r")
user_csvdata=csv.reader(fp)

users=list(user_csvdata)


for user in users:
    for data in user:
        print(data,end="\t")
    print()    
fp.close()        