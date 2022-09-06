# TODO: Create a new dict that takes each word in the sentence and calculates the number of letters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

# TODO: Convert temperature from C° to F°
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# new_dict = {new_key: new_value for (key,value) in dict.items()}
weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

# TODO: Iterate over pandas DataFrame
student_dict = {
    "student": ["Angela", "Chente", "Jojo"],
    "score": [56, 76, 98]
}

# Looping through a DataFrame
for (key, value) in student_dict.items():
    print(value)  # [56, 76, 98]

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through rows of a DataFrame
for (index, row) in student_data_frame.iterrows():
    print(row.student)  # Angela, Chente, Jojo
    print(row.score)    # 56, 76, 98

# DataFrame specifics
for (index, row) in student_data_frame.iterrows():
    if row.student == "Chente":
        print(row.score)    # 76