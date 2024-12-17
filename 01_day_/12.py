# 12)WAP to find the sum of all items in a dictionary
# Input: {'a': 100, 'b':200, 'c':300}
# Output: 600
# Input: {'x': 25, 'y':18, 'z':45}
# Output: 88

def sum_dict(aDict):
    sum=0
    for values in aDict:
        sum=sum+aDict[values]
    print(sum)

adict={'a': 100, 'b':200, 'c':300}
sum_dict(adict)