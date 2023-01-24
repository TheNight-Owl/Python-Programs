# WAP to print the pattern given below
# *****
# ****
# ***
# **
# *

n=int(input("Enter the no. of rows:\n"))
if n<=0:
    print("I have got nothing to print")
else:
    for i in range(n, 0 ,-1):
        print("*"*i)