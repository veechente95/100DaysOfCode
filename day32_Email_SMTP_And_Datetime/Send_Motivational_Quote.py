# TODO: Use the datetime and smtplib modules to email motivational quotes depending on the day of the week.
#  In this example, it is set to wednesday as the day of the week to send quote

import datetime as dt
import random
import smtplib

MY_EMAIL = "enter_email"
PASSWORD = "enter_password"


now = dt.datetime.now()     # give you current date and time
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt", mode="r") as quote_file:
        all_quotes = quote_file.readlines()
        random_quotes = random.choice(all_quotes)
    print(random_quotes)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()  # (TLS) Transport Layer Security -  secures connection w/ email server
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="enter_email",
            msg=f"Subject: Motivational Quote\n\n{random_quotes}"
        )

