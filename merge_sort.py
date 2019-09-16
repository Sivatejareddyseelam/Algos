def merge(l,r):
    i=j=k=0
    temp=[]
    while i<len(l) and j<len(r):
        if l[i]<=r[j]:
            temp.insert(k,l[i])
            i=i+1
        else:
            temp.insert(k,r[j])
            j=j+1
        k=k+1
    while i< len(l):
        temp.insert(k,l[i])
        k=k+1
        i=i+1
    while j< len(r):
        temp.insert(k,r[j])
        k=k+1
        j=j+1
    return temp
def merge_sort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        lef=merge_sort(left)
        rig=merge_sort(right)
        a=merge(lef,rig)
    else:
        a=l
    return a

l=[10]
print(merge_sort(l))