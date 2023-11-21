import time
import firebase_admin
from firebase_admin import credentials, db

def on_change(response):
    print(response.event_type)
    print(response.data)

cred = credentials.Certificate("./credentials.json")

firebase_admin.initialize_app(cred, {"databaseURL": "https://new-project-ad1f6-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference().child('microbit_log')

my_ref = ref.listen(on_change)

