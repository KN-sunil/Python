import mysql.connector

try:
    dbcon=mysql.connector.connect(
        host="localhost",user="root",
        password="root",database="8pm"
    )
    mycursor=dbcon.cursor()
    mycursor.execute('Select * from employee')
    empdata=mycursor.fetchall()

    for emp in empdata:
        print("Employee Id:", emp[0],"Employee Name:",emp[1],"and salary:", emp[2])


except mysql.connector.DatabaseError as err:
    if err:
        print("unable to connect database")

finally:
    mycursor.close()
    dbcon.close()


