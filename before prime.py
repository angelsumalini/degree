a=int(input("enter a starting range"))
for j in range(a-1,1,-1):
    for i in range(2,j):
        if j%i==0:
            #print(j,"is not a prime number")
            break
        else:
            bp=j
            print(j)
            break
