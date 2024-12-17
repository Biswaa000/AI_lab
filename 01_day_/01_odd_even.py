def isCheck(n):
    if n%2==0:
        print(f"The number {n} is even")
    else:
        print(f"The number {n} is odd.")

num=input("please enter numver:-")
num=int(num)
isCheck(num)