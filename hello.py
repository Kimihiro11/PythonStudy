import math
def my(a,b,c):
    x =0
    if a==0:
        x = -c/b
    elif a != 0:
        y = math.sqrt(b*b-4*a*c)
        x = ((-b+y)/2*a,(-b-y)/2*a)
    return x
print(my(2,8,4))