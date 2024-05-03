import json
fp1=open("users.json","r")
users=json.load(fp1)

male_data=[]
female_data=[]

#with filter function

male_data=list(filter(lambda user:user["gender"]=="Male",users))   
female_data=list(filter(lambda user:user["gender"]=="Female",users))

fp2=open("Male.json","w")
fp3=open("Female.json","w")
json.dump(male_data,fp2)
json.dump(female_data,fp3)


fp1.close()
fp2.close()
fp3.close()