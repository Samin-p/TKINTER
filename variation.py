from tkinter import *
def com():
    var1=kj.get()
    var2=kp.get()
    var3=y6work.get()
    var4=y7work.get()
    l=[]
    m=[]
    l.append(int(var1))
    l.append(int(var2))
    m.append(int(var3))
    m.append(int(var4))
    print(l,m)
    po=[]
    lou=[]
    for t,e in zip(l,m):
        po.append(t/e)
        lou.append(t*e)
    if len(set(po))==1:
        o=set(po)
        
        if 0 in o:
            if len(set(lou))==1:
                print("they are in inverse variation")
            else:
                print("Something wrog you have input")
        else:
            print("they are in direct variation")
    elif len(set(lou))==1:
        if len(set(lou))==1:
                print("they are in inverse variation")
        else:
                print("Something wrog you have input")

    else:
        print("Something wrog you have input")
m=Tk()
m.title("Variation")

op=Label(text="enter x:")
op.grid(column=0,row=0)
k=IntVar()
l=IntVar()
kj=Entry(textvariable=k)
kp=Entry(textvariable=l)
kj.grid(column=1,row=0)
kp.grid(column=2,row=0)


oq=Label(text="enter y:")
oq.grid(column=0,row=1)
y6=IntVar()
y7=IntVar()
y6work=Entry(textvariable=y6)
y7work=Entry(textvariable=y7)
y6work.grid(column=1,row=1)
y7work.grid(column=2,row=1)


sub=Button(text="Check",bg="skyblue",command=com)
sub.grid(row=2,column=1)

sub=Button(text="Check",bg="light yellow")
sub.grid(row=2,column=2)
m.mainloop()