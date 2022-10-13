n=int(input())
l=list(map(int,input().split()))
k=sum(l)
avg=k/n
print("{:.2f}".format(avg))