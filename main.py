#!/usr/bin/env python3
import time
import firebase_admin


from firebase_admin import credentials, db

cred = credentials.Certificate("./credentials.json")

firebase_admin.initialize_app(cred, {"databaseURL": "https://new-project-ad1f6-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference()


# ref.update({})
