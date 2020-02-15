import pymysql

# 创建mysql数据库连接
db = pymysql.connect('127.0.0.1', 'root', '', 'xiao', charset='utf8')
# 创建游标
cursor = db.cursor()
#用游标操作数据库
cursor.execute("insert into sanguo(id,name,address) values(2, 'sh', 'lv');")

#查询结果集所有数据
data = cursor.fetchall()
print(data)
#关闭游标
cursor.close()
#关闭数据库连接
db.close()

