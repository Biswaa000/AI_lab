from math import sqrt,ceil

def prime(a,b):
    
    for num in range(a,b+1):
        flag=0
        print(f"For {num}")
        for i in range(2,ceil(sqrt(num))):
            print(i)
            if num%i == 0:
                # print(f"{num} not prime number")
                flag =1
    
        if flag==0:
            print(f"{num}")

prime(3,6)
