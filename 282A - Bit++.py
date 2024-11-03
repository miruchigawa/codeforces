t,r=int(input()),0
for _ in range(t):
    n=input()
    r += 1 if "++" in n else -1
print(r)
