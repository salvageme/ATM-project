import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='root',database='ATM_MACHINE')
if conn.is_connected():
      print("sucessfully connected")
c1=conn.cursor()
c1.execute('drop table IF EXISTS records')
mn="CREATE TABLE RECORDS( ACCONT_NO  INT(6) zerofill primary key auto_increment,PASSWORD INT,NAME VARCHAR(20),PHONE_NO BIGINT unique check(PHONE_NO like'__________'),CR_AMT INT default(0),WITHDRAWL INT default(0),BALANCE INT default(0))"
c1.execute(mn)
print("Sucessfully created")
