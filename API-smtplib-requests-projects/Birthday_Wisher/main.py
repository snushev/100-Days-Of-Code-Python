#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import pandas as pd
import smtplib
import datetime as dt
import random

# Enter your email address and password
MY_EMAIL = "email@example.com"
PASSWORD = "password"

# Makes a list of available congratulations templates
files = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

# Takes today's date and month
now = dt.datetime.now()
today_month = now.month
today_day = now.day

# Takes the birthdays info for all people in the list
data = pd.read_csv("birthdays.csv")
birthdays = data.to_dict('records')


# Checks if any person has a birthday
for person in birthdays:
    if today_month == person['month'] and today_day == person['day']:

        # Chooses random template from the list
        chosen_file = random.choice(files)

        # Replaces the name in the template with the person's name'
        with open(chosen_file, "r") as file:
            letter_content = file.read()
            letter_content = letter_content.replace("[NAME]", person['name'])
        # Send the generated letter to that person's email address.
        with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person['email'],
                msg=f"Subject:Saturday Motivational Quote\n\n{letter_content}")


