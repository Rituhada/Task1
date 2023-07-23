from tkinter import *
root =Tk()
root.iconbitmap(r'calculator_xAm_icon.ico')
root.geometry("380x455")
root.resizable(False,False)
root.configure(bg="#ffffff")
root.title("CALCULATOR")

calculation=" "
def show(value):
    global calculation
    calculation+=value
    label.config(text=calculation)


def clear():
    global calculation
    calculation=""
    label.config(text=calculation)

def calculate():
    global calculation
    result=""
    if calculation!="":
        try:
            result=eval(calculation)
        except:
            result="error"
            calculation=""
    label.config(text=result)
    
label=Label(root,width=25,height=2,text="",font= "Cambira 30 ", bg="white")
label.pack()

Button(root,text="C", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:clear()).place(x=0,y=100)
Button(root,text="/", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("/")).place(x=95,y=100)
Button(root,text="%", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("%")).place(x=190,y=100)
Button(root,text="*", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("*")).place(x=280,y=100)

Button(root,text="9", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("9")).place(x=0,y=170)
Button(root,text="8", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("8")).place(x=95,y=170)
Button(root,text="7", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("7")).place(x=190,y=170)
Button(root,text="-", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("-")).place(x=280,y=170)

Button(root,text="6", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("6")).place(x=0,y=240)
Button(root,text="5", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("5")).place(x=95,y=240)
Button(root,text="4", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("4")).place(x=190,y=240)
Button(root,text="+", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("+")).place(x=280,y=240)

Button(root,text="3", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("3")).place(x=0,y=310)
Button(root,text="2", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("2")).place(x=95,y=310)
Button(root,text="1", width=4,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("1")).place(x=190,y=310)
Button(root,text="0", width=7,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show("0")).place(x=0,y=380)

Button(root,text=".", width=6,height=1, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:show(".")).place(x=145,y=380)
Button(root,text="=", width=4,height=3, font="Cambira 30 ",relief=GROOVE,bd=0,command=lambda:calculate()).place(x=280,y=300)
root.mainloop()
