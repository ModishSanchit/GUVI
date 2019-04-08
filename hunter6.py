num=int(input())
l=list(map(int,input().split()))
l1=[max(l)+1]*(max(l))
#print(l1)
for r in range(len(l)):
    for s in range(r+1,len(l)):
        if l[r]==l[s]:
            l1[l[r]]=s

print(l1.index(min(l1)))
