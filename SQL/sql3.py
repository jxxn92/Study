import pymysql as pm

conn = pm.connect(host = '127.0.0.1', user = 'root', password= '0000', db = 'soloDB', charset = 'utf8')
cur = conn.cursor()

cur.execute("SELECT * FROM userTable")

print("사용자ID          사용자이름        이메일     출생연도")
print("-----------------------------------------------------------------------")

while(1):
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s  %15s  %20s  %d" % (data1, data2, data3, data4))


conn.close()