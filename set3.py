ch = input()
l=['a','e','i','u','o','A','E','I','O','U']
count = 0
if ord(ch) >= 65 and ord(ch) <= 122:
	for i in l:
		if ch == i:
			count+=1
	if count > 0:
		print("Vowel")
	else:
		print("Consonent")
else:
	print("Invalid")
