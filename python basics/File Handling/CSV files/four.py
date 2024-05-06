import csv
fp=open("emp.csv","r")

emp_obj=csv.reader(fp)

employees=list(emp_obj)

for employee in employees:
    print("id:",employee[0],"name:",employee[1],"gender:",employee[2])

fp.close()    