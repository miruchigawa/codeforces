t=int(input())
for _ in range(t):
    n=input()
    print(n if len(n) <= 10 else "{}{}{}".format(n[0], len(n)-2, n[-1])) 
