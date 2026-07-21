"""
Simple Mail Transfer Protocol.
"""

import smtplib

my_email = "test@gmail.com"
my_password = ""

with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="test2@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email.",
    )
