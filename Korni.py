a=int(input())
b=int(input())
c=int(input())
d=b**2-4*a*c
if d==0:
    print("X1=", -b/(2*a))
if d<0:
    print("Kornej  net")
if d>0:
    print("X1=", (-b+d**0.5) / (2 * a))
    print("X2=", (-b-d**0.5) /(2 * a))