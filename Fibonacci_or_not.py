n=int(input())
n1=0
n2=1
n3=0
ch='False'
while(n3<=n):
    n3=n1+n2
    n1=n2
    n2=n3
    if n == n3:
        ch="True"
        break
print(ch)