
import firebase_admin
from firebase_admin import credentials

def initialize_firebase():
    # Initialize Firebase Admin SDK
    if not firebase_admin._apps:
        cred = credentials.Certificate('/path/to/your/serviceAccountKey.json')
        firebase_admin.initialize_app(cred)
