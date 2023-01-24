# WAP to print the pattern given below
# *****
#  ****
#   ***
#    **
#     *

n=int(input("Enter the no. of rows:\n"))
if n<=0:
    print("I have got nothing to print")
else:
    c=n
    for i in range(0, n):
        print(" "*i, end="")
        print("*"*c)
        c-=1