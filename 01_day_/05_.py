# marks=dict()

# for i in range(1,10):
#     mark=input("Enter the mark:")
#     marks[i]=mark
#     print(marks)

# new ways ---------------------------------
# def getmark(n):
#     mark=input("enter the number:")
#     markk=mark.split()
#     mark_

# Initialize an empty list to store marks
marks = []

# Input marks for 10 students
print("Enter the marks of 10 students:")
for i in range(10):
    while True:
        try:
            # Take input for each student's marks
            mark = float(input(f"Enter marks for student {i + 1}: "))
            if 0 <= mark <= 100:  # Assuming valid marks are between 0 and 100
                marks.append(mark)
                break
            else:
                print("Marks should be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Display the marks
print("\nMarks of the 10 students are:")
for i, mark in enumerate(marks, start=1):
    print(f"Student {i}: {mark}")
