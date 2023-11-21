import serial
from serial.tools import list_ports


import time
import firebase_admin
from firebase_admin import db, credentials

TIMEOUT = 0.1
PID_MICROBIT = 516
VID_MICROBIT = 3368

def find_comport(pid, vid, baud):
    """returns a serial port"""
    ser_port = serial.Serial(timeout=TIMEOUT)
    ser_port.baudrate = baud
    ports = list(list_ports.comports())
    # scanning ports
    for p in ports:
        try:
            print(f'Testing: \n\t port: {p!r} \n\t pid: {p.pid} \n\t vid: {p.vid}')
        except AttributeError:
            continue

        if p.pid == pid and p.vid == vid:
            ser_port.port = str(p.device)
            return ser_port
    return None


def main():
    cred = credentials.Certificate("./credentials.json")

    firebase_admin.initialize_app(cred, {"databaseURL": "https://new-project-ad1f6-default-rtdb.europe-west1.firebasedatabase.app/"})

    ref = db.reference()

    ref = ref.child('microbit_log')

    ser = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
    if not ser:
        print("microbit not found")
        return
    ser.open()

    while 1:
        mb_status = str(ser.readline().decode('utf-8'))
        mb_status = mb_status.strip().replace("\r\n", "")

        if mb_status.isdigit():
            print(mb_status)
            ref.update({int(time.time()) : {'light_status': int(mb_status)}})


if __name__ == '__main__':
    main()
