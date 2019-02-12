s=input()
c=0
for d in range(0,len(s)):
	if s[d].isnumeric() or s[d].isalpha():
		c=c+1
a=len(s)-c
print(a)
