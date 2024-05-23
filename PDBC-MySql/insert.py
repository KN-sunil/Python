import mysql.connector

try:
    dbcon=mysql.connector.connect(host="localhost",user='root',password='root',database='8pm')
    mycursor=dbcon.cursor()
    sql_st='''
             insert into employee values('101','sunil',50000,'banglore')

           '''
    mycursor.execute(sql_st)
    dbcon.commit()
    print('data inserted successfully')

except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    mycursor.close()
    dbcon.close()            