# You are going to write a program that calculates the average student height from a List of heights using for loops
# input: 156 178 165 171 187


student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print("Total height:", total_height)

num_of_students = 0
for student in student_heights:
    num_of_students += 1
print("Number of students:", num_of_students)

avg_height = round(total_height / num_of_students)
print("Average height:", avg_height)