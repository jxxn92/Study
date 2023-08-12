from tkinter import *

root = Tk()
root.title("Jxxn GUI")
root.geometry("640x480") # 가로 x 세로

chkvar = IntVar() # chkvar 에 int 형으로 값을 저장한다.
chkbox = Checkbutton(root, text = "오늘 하루 보지 않기", variable=chkvar)
# chkbox.deselect()
# chkbox.select()
chkbox.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크

btn = Button(root, text = "클릭", command = btncmd)
btn.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = "일주일 동안 보지 않기", variable=chkvar2)
chkbox2.pack()

root.mainloop()