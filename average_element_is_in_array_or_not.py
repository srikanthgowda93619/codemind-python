n=int(input())
l=list(map(int,input().split()))
m=sum(l)
k=m//n
if k in l:
    print("True")
else:
    print("False")