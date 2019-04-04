l = list(map(int,input().split()))
greatest=l[0]
for i in range(1,(len(l))):
    if l[i] > greatest:
        greatest = l[i]
print(greatest)
