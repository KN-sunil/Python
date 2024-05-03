import json
fp1=open("users.json","r")
users=json.load(fp1)

male_data=[]
female_data=[]

def getMale_users(user):
    return user["gender"]=="Male"          #instead of lambda function we are using normal function

def getFemale_users(user):
    return user["gender"]=="Female"  

male_data=list(filter(getMale_users,users))   
female_data=list(filter(getFemale_users,users)) 

fp2=open("Male.json","w")
fp3=open("Female.json","w")
json.dump(male_data,fp2)
json.dump(female_data,fp3)


fp1.close()
fp2.close()
fp3.close()