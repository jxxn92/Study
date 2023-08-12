id_pw = ["programmer01", "15789"]
fid = id_pw[0]
fpw = id_pw[1]
db = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]
id_pw_dict = {}
for i in range(len(db)):
    id_pw_dict[db[i][0]] = db[i][1]
if fid in id_pw_dict.keys():
    if id_pw_dict.get(fid) == fpw:
        print("login")
    else:
        print("wrong pw")
else:
    print("fail")