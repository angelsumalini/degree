n=int(input("enter a number"))
rev=0
a=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if rev==a:
    print(a,"is a palindrome number")
else:
    print(a,"is not a palindrome number")
