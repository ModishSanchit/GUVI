num=int(input())
lis=list(map(int,input().split()))
s=set()
for i in range(n):
    if i==lis[i]:
       s.add(i)
q=[print(str(i)+" ",end="") for i in s]
