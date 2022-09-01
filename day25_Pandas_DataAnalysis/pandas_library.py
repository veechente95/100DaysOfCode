import pandas
import csv

# TODO: pull list of temperatures from csv list using pandas
data = pandas.read_csv("./weather_data.csv")
print(data)
print(data["temp"])


# TODO: pull list of temperatures from csv list WITHOUT pandas
with open("./weather_data.csv", mode="r") as csv_data:
    data = csv.reader(csv_data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

