from tkinter import *
root=Tk()
root.title("calculator")
root.geometry("570x600+400+100")
root.config(bg="#658f87")
root.resizable(False,False)
label_result=Label(root,text="",font=("arial",40),height=2,width=25,background="#1f2424",fg="#a5a8a8")
label_result.pack()
visible_interface=""
def show(value):
    global visible_interface
    visible_interface+=value
    label_result.config(text=visible_interface)

def clear():
    global visible_interface
    visible_interface=""
    label_result.config(text=visible_interface)

def calculate():
    
    Result=""
    if visible_interface!="":
        try:
            Result=eval(visible_interface)
        except:
            Result="error"
    label_result.config(text=Result)



Button(root,text="C",width=5,height=1,font=("airal",30,"bold"),fg="white",bg="#eb7323",command=lambda: clear()).place(x=10,y=130)
Button(root,text="/",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("/")).place(x=150,y=130)
Button(root,text="%",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("%")).place(x=290,y=130)
Button(root,text="*",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("*")).place(x=430,y=130)

Button(root,text="7",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("7")).place(x=10,y=220)
Button(root,text="8",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("8")).place(x=150,y=220)
Button(root,text="9",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("9")).place(x=290,y=220)
Button(root,text="-",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("-")).place(x=430,y=220)

Button(root,text="4",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("4")).place(x=10,y=310)
Button(root,text="5",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("5")).place(x=150,y=310)
Button(root,text="6",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("6")).place(x=290,y=310)
Button(root,text="+",width=5,height=3,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("+")).place(x=430,y=310)



Button(root,text="1",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("1")).place(x=10,y=400)
Button(root,text="2",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("2")).place(x=150,y=400)
Button(root,text="3",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("3")).place(x=290,y=400)

Button(root,text="0",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show("0")).place(x=10,y=490)
Button(root,text=".",width=5,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= lambda:show(".")).place(x=150,y=490)
Button(root,text="=",width=11,height=1,font=("airal",30,"bold"),fg="#f3f5f2",bg="#262624",command= calculate).place(x=290,y=490)

outro=Label(root,text="enjoy coading @SAKIF").pack(side=BOTTOM)
icon=PhotoImage(file="calculator.png")
root.iconphoto(False,icon)
 

root.mainloop()
