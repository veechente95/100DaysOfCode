import pandas

# # TODO: pull list of temperatures from csv list using pandas
data = pandas.read_csv("./weather_data.csv")
# print(data["temp"])
#
# # TODO: convert data to dictionary separated by series (table headers)
# data_dict = data.to_dict()
# print(data_dict)
#
# # TODO: data series to a list
# temp_list = data["temp"].to_list()
# print(temp_list)        # [12, 14, 15, 14, 21, 22, 24]
# print(len(temp_list))   # 7
#
# # TODO 1): print average temp from csv data
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
#
# # TODO 2): print average temp from csv data using pandas
# print(data["temp"].mean())
#
# # TODO: print max temp
# print(data["temp"].max())
#
# # TODO: get data from columns
# print(data["condition"])
# print(data.condition)
#
# # TODO: get data from rows
# print(data[data.day == "Monday"])
# print(data[data["day"] == "Monday"])

# TODO: print the row of data that had the max temp
# print(data[data.temp == data.temp.max()])
#
# # what if we wanted that particular days condition
# monday = data[data.day == "Monday"]
# print(monday.condition)     # Sunny
#
# # convert Monday temp from celsius to fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)        # 53.6

# TODO: How to create a DataFrame from scratch
# TODO: How to save DataFrame to new CSV file

data_dict = {
    "students": ["Chente", "Marco", "Cesar", "Maribel"],
    "scores": [76, 56, 65, 69]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")