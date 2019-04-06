num = int(input())
l = list(map(int,input().split()))
a = max(l)
l1=[]
l2=[]
for i in range(0,a+1):
    l1.append(0)
for i in range(0,len(l)):
    l1[l[i]]+=1
print(l1)
for i in range(0,len(l1)):
    if l1[i] >1:
        l2.append(i)

for i in range(0,len(l2)):
    print(l2[i], end="")
