# WAP to sort the list {5, 4, 11, 13, 51} 

def sort_list(my_list):  # Bubble Sort
    for i in range(len(my_list)):  
        for j in range(len(my_list) - 1 - i):  
            if my_list[j] > my_list[j + 1]:  
                
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list  


my_list = [5,444,11,13,51]

original_list = my_list.copy()

sorted_list = sort_list(my_list)
print(sorted_list)