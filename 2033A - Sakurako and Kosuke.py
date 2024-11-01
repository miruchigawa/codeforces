t=int(input())
for _ in range(t):
    n=int(input())
    x,i=0,1
    while True:
        m=2*i-1
        if i%2 == 1:
            x -= m 
            if abs(x) > n:
                print("Sakurako")
                break
        else:
            x += m
            if abs(x) > n:
                print("Kosuke")
                break
        i += 1
