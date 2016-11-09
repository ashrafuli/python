def oe(x):
    if x%2==0:
        return(0)
    else:
        return(1)
l=[]
for i in range(50,100):
    if oe(i):
       l.append(i)
print("odd list 50 to 100:",l)
