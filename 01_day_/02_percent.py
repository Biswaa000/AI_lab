def result(n):
    if n>=80:
        print("Distinction")

    elif 65<=n<=80:
        print("First Division")
    elif 55<=n<=65:
        print("Second Division")
    elif 40<=n<=55:
        print("Third Division")

    else:
        print('Fail')

n=int(input("enter:"))
result(n)
