import os
import pandas
import smtplib
import datetime
import random

#-----------------------------------MY DATA---------------------------------------------#
email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
#---------------------------------------------------------------------------------------#

birthdays = pandas.read_csv('birthdays.csv')
birthdays = birthdays.to_dict(orient='records')

letters_list =  []
with open('letter_templates/letter_1.txt', 'r') as file:
    x = file.read()
    letters_list.append(x)

with open('letter_templates/letter_2.txt', 'r') as file:
    x = file.read()
    letters_list.append(x)

with open('letter_templates/letter_3.txt', 'r') as file:
    x = file.read()
    letters_list.append(x)

now = datetime.datetime.now()
now_month = now.month
now_day = now.day

to_send_letter = []

for name in birthdays:
  if name["month"] == now_month and name["day"] == now_day:
    random_letter = random.choice(letters_list)
    random_letter = random_letter.replace("[NAME]",name["name"])
    to_send_letter = random_letter

    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(from_addr=email, to_addrs=name["email"],msg=f"Subject:Happy Birthday!\n\n{to_send_letter}")

    print("Sent")
  else:
    print("Nothing to do")
