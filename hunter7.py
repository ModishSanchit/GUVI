num = int(input())
lis = list(map(int,input().split()))
res_list=[]
for i in range(0,len(lis)):
    if(lis[i]%2 == 0 and i % 2 !=0):
        res_list.append(lis[i])
    if(lis[i]%2 != 0 and i % 2 == 0):
        res_list.append(lis[i])

for i in res_list:
    print(res_list)
