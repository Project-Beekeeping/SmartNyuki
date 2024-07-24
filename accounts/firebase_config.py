import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

# Replace with the path to your downloaded service account key file
cred = credentials.Certificate('/home/hp/Desktop/CODES/SmartNyuki/project-login2-6c049-firebase-adminsdk-gh0yz-c6e5174321.json')
firebase_admin.initialize_app(cred)
