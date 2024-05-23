import mysql.connector

try:
    dbcon=mysql.connector.connect(
        host="localhost",user="root",password="root",database="8pm")
    mycursor=dbcon.cursor()
    sql_st = ''' delete from employee where eid=105 '''
               
    mycursor.execute(sql_st)

    dbcon.commit()
    print("deleted succefully")

except mysql.connector.DatabaseError as err:
    if err:
        print("unable to connect to database")

finally:
    dbcon.close()            