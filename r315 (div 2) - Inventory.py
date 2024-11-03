l = int(input())
v = list(map(int, input().split()))
o = [0] * (l + 1)
d = []

for i, n in enumerate(v):
    if 1 <= n <= l and o[n] == 0:
        o[n] = 1  
    else:
        d.append(i)  

m = [i for i in range(1, l + 1) if o[i] == 0]

for i in range(len(d)):
    v[d[i]] = m[i]

print(" ".join(map(str, v)))
