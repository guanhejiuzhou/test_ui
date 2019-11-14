import cx_Oracle
import time

def Sqlku():
    # 获取一个数据库连接
    db = cx_Oracle.connect('hzero/hzero@172.20.0.201:1521/xe')
    cur = db.cursor()  # 游标操作
    sql1 = "SELECT column_name,table_name FROM user_tab_columns WHERE column_name='TENANT_ID_' "
    cur.execute(sql1)  # 实行参数中的sql命令
    rows = cur.fetchall()  # 获取数据
    return rows


def Sqlbiao():
    # 获取一个数据库连接
    db = cx_Oracle.connect('hzero/hzero@172.20.0.201:1521/xe')
    cur = db.cursor()  # 游标操作
    listCS = []

    listSQL = Sqlku()
    #print(listSQL)
    for sqlq in listSQL:
        print(sqlq[1])
        sql2 = "SELECT * FROM %s WHERE TENANT_ID_ =0;"%sqlq[1]
        #sql2 = "UPDATE %s SET  TENANT_ID_ =1 WHERE TENANT_ID_ =0;"%sqlq[1]  # 修改字段值
        print(sql2)
        try:
            cur.execute(sql2)  # 实行参数中的sql命令
            rows = cur.fetchall()  # 获取数据
            listCS.append(rows)
        except:
            time.sleep(1)

    print(listCS)
    return listCS

Sqlbiao()