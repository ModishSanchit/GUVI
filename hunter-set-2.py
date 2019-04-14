s = input()
l = list(s.split(" "))
print([x[::-1] for x in l],end="")
