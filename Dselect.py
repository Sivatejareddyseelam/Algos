def partion(a,p):
    piv=a.index(p)
    b=a[0]
    a[0]=p
    a[piv]=b
    i=0
    for j in range(1,len(a)):
        if a[j]<p:
            d=a[i+1]
            a[i+1]=a[j]
            a[j]=d
            i=i+1
    z=a[i]
    a[i]=p
    a[piv]=z
    return i

def Dselect(a,k):
    if len(a)==1:
        return a[0]
    else:
        if len(a)<5:
            p=a[len(a)//2]

        else:
            n=len(a)
            siz=n//5
            parts=[]
            for i in range(0,siz):
                parts.append(a[i*n//siz:(i+1)*n//siz])
            print("parts")
            print(parts)
            c=[]
            for i in parts:
                i.sort()
                m=i[len(i)//2]
                c.append(m)
            print("c")
            print(c)
            p=Dselect(c,len(c)//2)
            print("p")
            print(p)
        xpart=partion(a,p)
        if xpart==k:
            return a[k]
        elif xpart>k:
            return Dselect(a[:xpart],k)
        else:
            k=k-xpart
            return Dselect(a[xpart+1:],k)
a=[2,5,7,4,10,9,6,1,0,13]
for i in range(0,len(a)):
    print("i",i)
    print("Dselect",Dselect(a,i))
