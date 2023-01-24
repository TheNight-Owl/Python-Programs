# WAP to print the pattern given below
#       *
#      ***
#     *****
#    *******

n=int(input("Enter the no. of rows:\n"))
if n<=0:
    print("I have got nothing to print")
else:
    c=1
    k=n-1
    for i in range(n):
        print(" "*k, end="")
        print("*"*c)
        c+=2
        k-=1