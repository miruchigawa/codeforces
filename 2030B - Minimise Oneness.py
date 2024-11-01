t=int(input())
for _ in range(t):
    n=int(input())
    print("".join(["01"[not i] for i in range(n)]))
