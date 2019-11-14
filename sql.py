import time
import cx_Oracle


def Sqlku(self):
    # 获取一个数据库连接
    self.connection = cx_Oracle.connect(host='172.20.0.201', user='hzero', passwd='hzero', db='HZERO', port=1521,
                                      charset='utf8mb4')

    sql1 = "select table_name from information_schema.tables where table_schema='库名';"

    with self.connection.cursor() as cursor:  # 设置游标---使用改链接创建并返回游标
        cursor.execute(sql1)  # 实行参数中的sql命令
        sqlreturn = cursor.fetchone()
        sqlreturn_str = str(sqlreturn[0])

    self.connection.commit()

    return sqlreturn_str


def Sqlbiao(self):
    # 获取一个数据库连接
    self.connection = cx_Oracle.connect(host='172.20.0.201', user='hzero', passwd='hzero', db='HZERO', port=1521,
                                      charset='utf8mb4')
    listCS = []

    listSQL = Sqlku()
    for s in listSQL:
        sql2 = "SELECT * FROM %s WHERE TENANT_ID_ =0" % (s)

    try:
        with self.connection.cursor() as cursor:  # 设置游标---使用改链接创建并返回游标
            cursor.execute(sql2)  # 实行参数中的sql命令
            Bsqlreturn = cursor.fetchone()
            Bsqlreturn_str = str(Bsqlreturn[0])
            self.connection.commit()

            listCS.append(Bsqlreturn_str)
    except:
        time.sleep(1)

    print(listCS)
    return listCS