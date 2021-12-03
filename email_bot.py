# October 2021 - v0.2
# A bot to email a specific body and message to a set list of people on either an xcel or csv sheet
# Looking to expand to other file types and connect to UI if possible
# @author Team 2


import smtplib
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
import config

FILENAME = 'testEmailList.xlsx'
EMAIL_ADDRESS = ''
PASSWORD = ''
TARGET_VAL = 2.0

plant_number = 0


# def get_moisture_level():
# Get plant number inside of this function as well if possible

# def add_recipient(address):


def get_recipients_xlsx():
    data = pd.read_excel(FILENAME, sheet_name=0)
    print(data)
    stats = pd.DataFrame()
    print(stats)

    list_recipients = data['Email List']
    return list_recipients


def send_mail(subject, msg, lis):
    message = 'Subject: {}\n\n{}'.format(subject, msg)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()

    server.login(config.EMAIL_ADDRESS, config.PASSWORD)

    for recipient in lis:
        server.sendmail(config.EMAIL_ADDRESS, recipient, message)

    server.quit()
    print("Server closed, success!")


def recent_five(lis):
    for x in range(-1, -5):
        print(lis[x])


# Main Script

# Add if/else statement to determine how low the moisture reading is and reply accordingly.
# if moisture_level < TARGETVAL / 2:
#     subject = "Soil Moisture level on Plant #{} is extremely low!".format(plant_number)
#     body = 'You should probably water this immediately, thanks for using our automatic Soil Moisture Sensor!"
# elif moisture_level < TARGETVAL:
#     subject = "Soil Moisture level on Plant #{} is getting low!".format(plant_number)
#     body = "Might want to consider watering that bad boy, thanks for using our automatic Soil Moisture Sensor!"


subject = "Soil Moisture on Plant #1 is low!"
body = "It is highly recommended to water your plant :) Thanks so much for using our automatic Soil Moisture Sensor!"
recipients = get_recipients_xlsx()
print("Recipients obtained")
send_mail(subject, body, recipients)
