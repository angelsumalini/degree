n=int(input("enter a number"))
a=n
s=0
while n>0:
      rem=n%10
      s+=rem
      n//=10
if a%s==0:
      print(a,"is a harshad number")
else:
      print(a,"is not a harshad number")
