from tkinter import *

root = Tk()
root.title("Jxxn GUI")
root.geometry("640x480") # 가로 x 세로

txt = Text(root, width =30 , height = 5) # 여러 줄
txt.pack()
txt.insert(END, "글자를 입력하세요.")

e = Entry(root, width = 30) # 한 줄
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0",END)) # 1 : 첫번째 라인, 0 : 0번째 Column 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()