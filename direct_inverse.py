l=[]
n=[]
for i in range(2):
        
    c=int(input("Input x"))
    l.append(c)
    b=int(input("Input y"))
    n.append(b)

po=[]
lou=[]
for n,m in zip(l,n):
    k=n//m
    p=n

    lo=n*m
    po.append(k)
    lou.append(lo)
print(po)
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