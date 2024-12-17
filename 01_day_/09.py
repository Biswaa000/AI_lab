def summ(nums):
    sum =0 
    max=nums[0]

    for i in range(0,len(nums)):

        sum=sum+nums[i]
        if nums[i]>max:
            max=nums[i]
    return sum,max
 
    

q_list=[5,3,3,3,1,100]
print(summ(q_list))