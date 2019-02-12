g=list(map(int,input().split()))
m=0
for k in range(0,len(g)):
	if g[k]>m:
		m=g[k]
print(m)
