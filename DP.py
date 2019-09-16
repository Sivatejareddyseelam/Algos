"""
l=[1,2,3,4,5]
a=[]
a.append(0)
a.append(l[0])
for i in range(1,len(l)):
    if a[i]>a[i-1]+l[i]:
        m=a[i]
    else:
        m=a[i-1]+l[i]
    a.append(m)
print(a)
"""
#knapsack Problem
v=[3,2,4,4]
w=[4,3,2,3]
W=6
n=len(v)
A=[[0 for x in range(W+1)]for x in range(n+1)]
for i in range(1,n+1):
    for j in range(1,W+1):
        if w[i-1]>j:
            A[i][j]=A[i-1][j]
        else:
            A[i][j]=max(((A[i-1][j-(w[i-1])])+v[i-1]) ,A[i-1][j])
print(A)
