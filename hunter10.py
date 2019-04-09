lis=list(map(int,input().split()))
lis1=list(map(int,input().split()))
lis2=list(map(int,input().split()))
count=0
for i in range(0,len(lis2)):
    for j in range(0,len(lis1)):
        if(lis2[i] == lis1[j]):
            count+=1
if count == len(lis2):
    print("YES")
else:
    print("NO")
