# WAP to print the pattern given below
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

n=int(input("Enter the no. of rows:\n"))
if n<=0:
    print("I have got nothing to print")
else:
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==1 or i==n:
                print("*", end="")
            else:
                if j==1 or j==n:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()