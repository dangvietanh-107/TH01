#vd1
import mysql.connector
 #Create the connection object
myconn = mysql.connector.connect(host = "localhost", user = "root", 
 passwd = "")
 
#printing the connection object
print(myconn)

#vd2 tạo đối tượng connection:
import mysql.connector
 
# tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root", 
 passwd = "")
 
# in đối tượng connection ra màn hình
print(myconn)

#vd3
import mysql.connector
 
# tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root", 
 passwd = "", database = "test1")
# in đối tượng connection ra màn hình
print(myconn)

#vd4
import mysql.connector
 
# tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root", 
 passwd = "", database = "test1")
# in đối tượng connection ra màn hình
print(myconn)
# tạo đối tượng cursor
cur = myconn.cursor()
# in đối tượng cursor ra màn hình
print(cur)

#vd5
import mysql.connector
 
# tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root", 
 passwd = "")
# tạo đối tượng cursor
cur = myconn.cursor()
try:
 dbs = cur.execute("show databases")
except:
 myconn.rollback()
for x in cur:
 print(x)
myconn.close()

#vd6
import mysql.connector
 
# tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root", 
 passwd = "")
# tạo đối tượng cursor
cur = myconn.cursor()
try:
 cur.execute("create database PythonDB")
 dbs = cur.execute("show databases")
except:
 myconn.rollback()
for x in cur:
 print(x)
myconn.close()

#vd7
import mysql.connector
# tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root",
 passwd = "", database = "PythonDB")
 
# tạo đối tượng cursor
cur = myconn.cursor()
 
try:
 # tạo bảng Employee gồm 4 cột name, id, salary, và department id
 dbs = cur.execute("create table Employee(name varchar(20) not null, "
 + "id int(20) not null primary key, salary float not null, "
 + "dept_id int not null)")
except:
 myconn.rollback()
myconn.close()

#vd8
import mysql.connector
# tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root",
 passwd = "", database = "PythonDB")
 
# tạo đối tượng cursor
cur = myconn.cursor()
 
try:
 # thêm cột branch name vào bảng Employee
 cur.execute("alter table Employee add branch_name varchar(20) not null")
except:
 myconn.rollback()
myconn.close()

#vd9
import mysql.connector
#tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root",
 passwd = "", database = "PythonDB")
#tạo đối tượng cursor
cur = myconn.cursor()
sql = ("insert into Employee(name, id, salary, dept_id, branch_name) "
 + "values (%s, %s, %s, %s, %s)")
#giá trị của một row được cung cấp dưới dạng tuple
val = ("The Mac", 10001, 25000.00, 101, "Hanoi")
try:
 #inserting the values into the table
 cur.execute(sql,val)
 #commit the transaction
 myconn.commit()
except:
 myconn.rollback()
print(cur.rowcount,"record inserted!")
myconn.close()

#vd10
import mysql.connector
#tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root",
 passwd = "", database = "PythonDB")
#tạo đối tượng cursor
cur = myconn.cursor()
sql = ("insert into Employee(name, id, salary, dept_id, branch_name) "
 "values (%s, %s, %s, %s, %s)")
#giá trị của một row được cung cấp dưới dạng tuple
val = [("Vinh", 10002, 26000.00, 101, "Hanoi"), 
 ("Trung", 10003, 26000.00, 102, "Danang")]
try:
 #inserting the values into the table
 cur.executemany(sql, val)
 #commit the transaction
 myconn.commit()
except:
 myconn.rollback()
print(cur.rowcount,"record inserted!")
myconn.close()

#vd11
import mysql.connector
#tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root",
 passwd = "1234567890", database = "PythonDB")
#tạo đối tượng cursor
cur = myconn.cursor()
try:
 # select dữ liệu từ database
 cur.execute("SELECT * FROM Employee")
 
 # tìm nạp các hàng từ đối tượng con trỏ
 result = cur.fetchall()
 for x in result:
  print(x); 
except:
 myconn.rollback()
myconn.close()

#vd12
import mysql.connector
#tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root",
 passwd = "1234567890", database = "PythonDB")
#tạo đối tượng cursor
cur = myconn.cursor()
try:
 # select dữ liệu từ database
 cur.execute("SELECT name, id, salary FROM Employee")
 
 # tìm nạp các hàng từ đối tượng con trỏ
 result = cur.fetchall()
 for x in result:
  print(x); 
except:
 myconn.rollback()
myconn.close()

#vd13
import mysql.connector
#tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root",
 passwd = "1234567890", database = "PythonDB")
#tạo đối tượng cursor
cur = myconn.cursor()
try:
 # select dữ liệu từ database
 cur.execute("SELECT name, id, salary FROM Employee")
 
 # tìm nạp hàng đầu tiên từ đối tượng con trỏ
 result = cur.fetchone()
 print(result);
 
 # tìm nạp hàng tiếp theo từ đối tượng con trỏ
 result = cur.fetchone()
 print(result);
except:
 myconn.rollback()
myconn.close()

#vd14
import mysql.connector
#tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root",
 passwd = "1234567890", database = "PythonDB")
#tạo đối tượng cursor
cur = myconn.cursor()
try:
 # select dữ liệu từ database
 cur.execute("SELECT name, id, salary FROM Employee")
 
 # tìm nạp các hàng từ đối tượng con trỏ
 result = cur.fetchall()
 print("Name ID Salary")
 
 for row in result:
   print("%s %d %d"%(row[0],row[1],row[2]))
except:
 myconn.rollback()

#vd15
import mysql.connector
#tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root",
 passwd = "", database = "PythonDB")
#tạo đối tượng cursor
cur = myconn.cursor()
try:
 # cập nhật name cho bảng Employee
 cur.execute("update Employee set name = 'Đạt' where id = 10001")
 myconn.commit()
except:
 myconn.rollback()
myconn.close()

#vd16
import mysql.connector
#tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root",
 passwd = "", database = "PythonDB")
#tạo đối tượng cursor
cur = myconn.cursor()
try:
 # cập nhật name cho bảng Employee
 cur.execute("delete from Employee where id = 10001")
 myconn.commit()
except:
 myconn.rollback()
myconn.close()

 
