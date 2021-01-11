for _ in range(int(input())):
    n,k,d=map(int,input().split())
    a=list(map(int,input().split()))
    s=0
    for i in a:
        s+=i
    ans=s//k
    if ans<=d:
        print(ans)
    else:
        print(d)
