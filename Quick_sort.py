import random
def partion(a,l,r):
    pi=random.randint(l,r)
    f=a[l]
    a[l]=a[pi]
    a[pi]=f
    piv=a[l]
    i=l+1
    for j in range(l+1,r+1): #check this back later
         if a[j]<piv:
             b=a[i]
             a[i]=a[j]
             a[j]=b
             i=i+1
    c=a[i-1]
    a[i-1]=piv
    a[l]=c
    return i-1
def quicksort(a,i,j):
    if i<j:
        pi=partion(a,i,j)
        quicksort(a,i,pi-1)
        quicksort(a,pi+1,j)
    return a
a=[2,5,7,4,10,9,6,1,0]
i=0
j=len(a)
print(quicksort(a,i,j-1))
def Rselect(a,k):
    if len(a)==1:
        return a[0]
    else:
        x=partion(a,0,len(a)-1)
        if x==k:
            return a[k]
        elif x>k:
            return Rselect(a[:x-1],k)
        else:
            k=k-x
            return Rselect(a[x:],k)

for i in range(0,len(a)):
    print(Rselect(a,i))
