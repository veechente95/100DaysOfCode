from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "enter_email"
PASSWORD = "enter_password"

# TODO 1. Update the birthdays.csv with details.
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.

# TODO 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime.
# HINT 2: Use pandas to read the birthdays.csv
# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv. It should look like this:
        ## birthdays_dict = {
        ##     (12, 24): Angela,angela@email.com,1995,12,24
        ## }
# HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

today = datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# TODO: 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates
#  and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter.
# HINT 2: Use the random module to get a number between 1-3 to pick a random letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name.
    # https://www.w3schools.com/python/ref_string_replace.asp

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, mode="r") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

# TODO: 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()  # (TLS) Transport Layer Security -  secures connection w/ email server
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!!!\n\n{contents}"
        )


