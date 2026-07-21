import datetime as dt
import random
import smtplib

my_email = "test@gmail.com"
my_password = "senha"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        current_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test2@gmail.com",
            msg=f"Subject:Monday Quote Motivation\n\n{current_quote}",
        )
