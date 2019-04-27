#coding:utf-8

from dbConnecttion import MySqlConn
from _sqlite3 import Row

#申请资源
mysql = MySqlConn.Mysql()

sql = "SELECT * FROM T_REGION"
result = mysql.getMany(sql, 2)
print(result)

#释放资源
mysql.dispose()