from tkinter import *
root=Tk()
root.title("calculator")
root.geometry("570x600+100+200")
root.config(bg="#658f87")
root.resizable(False,False)
label_result=Label(root,text="",font=("arial",40),height=2,width=25)
label_result.pack()
equation=""
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    Result=""
    if equation!="":
        try:
            Result=eval(equation)
        except:
            Result="error"
    label_result.config(text=Result)



Button(root,text="C",width=5,height=1,font=("airal",30,"bold"),fg="#f0831d",bg="#262624",command=lambda: clear()).place(x=10,y=140)
Button(root,text="/",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("/")).place(x=150,y=140)
Button(root,text="%",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("%")).place(x=290,y=140)
Button(root,text="*",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("*")).place(x=430,y=140)

Button(root,text="7",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("7")).place(x=10,y=240)
Button(root,text="8",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("8")).place(x=150,y=240)
Button(root,text="9",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("9")).place(x=290,y=240)
Button(root,text="-",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("-")).place(x=430,y=240)

Button(root,text="4",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("4")).place(x=10,y=340)
Button(root,text="5",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("5")).place(x=150,y=340)
Button(root,text="6",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("6")).place(x=290,y=340)
Button(root,text="+",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("+")).place(x=430,y=340)



Button(root,text="1",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("1")).place(x=10,y=440)
Button(root,text="2",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("2")).place(x=150,y=440)
Button(root,text="3",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("3")).place(x=290,y=440)
Button(root,text="0",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("0")).place(x=430,y=440)

Button(root,text=".",width=12,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show(".")).place(x=10,y=530)
Button(root,text="=",width=12,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= calculate).place(x=300,y=530)


 

root.mainloop()