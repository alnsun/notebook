import MySQLdb
from consts import HOSTNAME, USERNAME, DATABASE, PASSWORD


con = MySQLdb.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)

with con as cur:
    cur.execute('drop table if exists users')
    cur.execute('create table users(id INT PRIMARY KEY AUTO_INCREMENT,'
            'name VARCHAR(25))')
    cur.execute('insert into users(name) values("zhangsan")')
    cur.execute('insert into users(name) values("lisi")')
    cur.execute('select * from users')

    rows = cur.fetchall()
    for row in rows:
        print row
    cur.execute('update users set name=%s where id=%s', ('wangwu', 1))
    print 'Number of rows updated:', cur.rowcount

    cur = con.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('select * from users')

    rows = cur.fetchall()
    for row in rows:
        print row['id'], row['name']

# Use with equals to blow
# try:
#     cur = con.cursor()
#     cur.execute('insert into users(name) values("zhaoliu")')
#     con.commit()
# except MySQLdb.Error as e:
#     con.rollback()
#
