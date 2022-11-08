n=int(input())
m=int(input())
cnt=0
for i in range(n,m+1):
    if i>1:
        for val in range(2,i):
            if i%val==0:
                break
        else:
            print(i)
                