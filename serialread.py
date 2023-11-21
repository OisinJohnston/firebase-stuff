import serial

import time
import firebase_admin
from firebase_admin import *


cred = credentials.Certificate("./credentials.json")

firebase_admin.initialize_app(cred, {"databaseURL": "https://new-project-ad1f6-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference()

ref.update({'temperature_log': ''})
ref = ref.child('temperature_log')

ser = serial.Serial()

ser.baudrate = 115200

ser.port = "COM3"

ser.open()

source = input("Enter the data source : ")

while 1:
    mb_temp = str(ser.readline().decode('utf-8'))

    mb_temp = mb_temp.strip().replace("\r\n", "")

    if mb_temp.isdigit():
        ref.update({str(int(time.time())) : {'Temperature': mb_temp, 'Location': source}})
    
    print(mb_temperature)
