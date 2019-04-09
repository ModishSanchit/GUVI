n1=map(int,input().split())
b=list(map(int,input().split()))
l=[]
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i]+b[j]==0:
            l.append([b[i],b[j]])
for i in range(2):
    print(l[0][i],end=" ")
