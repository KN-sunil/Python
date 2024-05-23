import mysql.connector

try:
    dbcon=mysql.connector.connect(
        host="localhost",user="root",password="root",database="8pm")
    mycursor=dbcon.cursor()
    sql_st = ''' update employee set esal=90000 where esal=50000 '''
               
    mycursor.execute(sql_st)

    dbcon.commit()
    print("updated succefully")

except mysql.connector.DatabaseError as err:
    if err:
        print("unable to connect to database")

finally:
    dbcon.close()            