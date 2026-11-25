import tkinter as tk
import math
window=tk.Tk()
window.title("Scientific Calculator")
window.geometry("520x650")
window.config(bg="black")
history=[]
entry=tk.Entry(window,font=("Arial",22),justify="right",bg="white")
entry.pack(fill="x",padx=10,pady=10,ipady=10)
def sin(x):
    return math.sin(math.radians(x))
def cos(x):
    return math.cos(math.radians(x))
def tan(x):
    return math.tan(math.radians(x))
def log(x):
    return math.log10(x)
def ln(x):
    return math.log(x)
def append(value):
    entry.insert(tk.END,value)
def clear():
    entry.delete(0,tk.END)
def calculate():
    try:
        expr=entry.get()
        expr=expr.replace("sqrt(","math.sqrt(")
        expr=expr.replace("^","**") 
        expr=expr.replace("pi","math.pi") 
        expr=expr.replace("%","/100")
        if expr.count("(")>expr.count(")"):
           expr=expr+")"*(expr.count("(")-expr.count(")"))
        result=str(eval(expr))
        history.append(entry.get()+"="+ result)
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")
def show_history():
    entry.delete(0,tk.END)
    if len(history)==0:
       entry.insert(0,"No History")
    else:
       entry.insert(0,history[-1])
frame=tk.Frame(window,bg="black")
frame.pack()
buttons=[
    "C","(",")","%","/",
    "sin","7","8","9","*",
    "cos","4","5","6","-",
    "tan","1","2","3","+",
    "log","0",".","=","sqrt",
    "ln","pi","e","^","History"
]
row=0
col=0
for char in buttons:
    if char=="C":
       b=tk.Button(frame,text=char,width=6,height=2,font=("Arial",14),bg="white",command=clear)
    elif char=="=":
       b=tk.Button(frame,text=char,width=6,height=2,font=("Arial",14),bg="orange",fg="white",command=calculate)
    elif char=="History":
       b=tk.Button(frame,text=char,width=6,height=2,font=("Arial",14),bg="blue",fg="white",command=show_history)
    elif char in ["sin","cos","tan","log","ln","sqrt"]:
       b=tk.Button(frame,text=char,width=6,height=2,font=("Arial",14),bg="purple",fg="white",command=lambda c=char: append(c +"("))
    else:
       b=tk.Button(frame,text=char,width=5,height=2,font=("Arial",14),bg="white",command=lambda c=char: append(c)) 
    b.grid(row=row,column=col,sticky="nsew",padx=2,pady=2)
    col += 1
    if col>4:
        col=0
        row+=1
window.mainloop()







