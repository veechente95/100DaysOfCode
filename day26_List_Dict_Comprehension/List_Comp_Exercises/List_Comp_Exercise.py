# TODO 1) Create a new numbers list with squared numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

# TODO 2) Create a new numbers list if number is even
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print(result)

# TODO 3) Create a list of numbers that are found in file1.txt AND file2.txt
with open("file1.txt", mode="r") as file1:
    file_1_data = file1.readlines()

with open("file2.txt", mode="r") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]
print(result)