t=int(input())
i=0
for _ in range(t):
    n=input()
    c=list(map(int, n.split())) 
    i += sum(c) >= 2
print(i)
