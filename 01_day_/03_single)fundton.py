def func(a,b):
    sum=a+b
    diff=a-b
    product=a*b
    quotient=a/b
    return sum, diff, product, quotient 

a=int(input("enter a:"))
b=int(input("enter b:"))
s, d, p, q = func(a,b)
ans=func(a,b)
print(ans)