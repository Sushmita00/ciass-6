# write a function to test if a number entered by the user is Armstrong or not. armstrong number e.g-371
# 3^3 +7^3+1^3=317

def armstrong(num):
    n=num
    sum=0
    while n>0:
        pow=n%10
        sum=sum+(pow*pow*pow)
        n=int(n/10)
    if sum==num:
         return 1
    else:
         return 0
m=int(input("enter the value"))
if armstrong(m):
    print("%d is armstrong number",m)
else:
    print("%d is not an armstrong number",m)


# write a function to check if a number is reverse of the number i.e.palindrome
#eg=12321 is palindrome

def palindrome(num):
    n=num
    sum=0
    while n>0:
        rem=n%10
        sum=(rem*10)+sum
        n=int(n/10)
    if sum==num:
        return 1
    else:
        return 0
n=int(input("enter the number"))
if palindrome(n):
        print("%d is a palindrome",n)
else:
        print("%d is a palindrome",n)
