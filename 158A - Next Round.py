_,k=map(int, input().split())
s=list(map(int, input().split()))
print(sum(1 for s_ in s if s_ >= s[k-1] and s_ > 0))
