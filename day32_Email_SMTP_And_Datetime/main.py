import smtplib

my_email = "email@gmail.com"
password = "password"

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()       # (TLS) Transport Layer Security -  secures connection w/ email server
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="to_email@gmail.com",
        msg="Subject: Hello World!\n\nTest. This is the body text of my email"
    )
