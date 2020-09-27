n=int(input("enter a number"))
s=0
a=n
while n>0:
    rem=n%10
    print(rem,"rem value")
    s+=rem*rem*rem
    print(s,"s value")
    n=n//10
    print(n,"n value")

if a==s:
    print(a," is a Armstrong number")
else:
    print(a,"is not a Armstrong number")
