# cook your dish here
n=int(input())
l=[]
for i in range(1,10):
    if n%i==0:
        l.append(i)
print(max(l))
