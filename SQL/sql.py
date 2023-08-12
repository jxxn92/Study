import pymysql as pm

conn = pm.connect(host = '127.0.0.1', user = 'root', password= '0000', db = 'soloDB', charset = 'utf8')

cur = conn.cursor()

cur.execute("CREATE TABLE userTable(id CHAR(4), userName CHAR(15), email CHAR(20), birthYear INT)")

cur.execute("INSERT INTO userTable VALUES('hong', '홍지윤', 'hong@naver.com', 1996)")
cur.execute("INSERT INTO userTable VALUES('kim', '김태연', 'kim@daum.net', 2011)")
cur.execute("INSERT INTO userTable VALUES('star', '별사랑', 'star@paran.com', 1990)")
cur.execute("INSERT INTO userTable VALUES('yang', '양지은', 'yang@gmail.com', 1993)")

conn.commit()

conn.close()



