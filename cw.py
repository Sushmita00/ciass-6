'''
# write a function to find the area of a circle. the value of the radius must be entered by the user.
pi=3.14
def area(r):
    print("the area of circle is",pi*r*r)
a=int(input("enter the valur of radius"))
area(a)


'''
#write a function pow(a,b).the function should return the value a rised  to the power of b.(a^b).
#hints=in python 2**3=8


def pow(a,b):
    c=a**b
    return(c)
h=int(input("enter the value of h"))
g=int(input("enter the value of g"))
c=pow(h,g)
print("enter the value of a^b is",c)