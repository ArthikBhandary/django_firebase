import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyD3iTzKeUcWaKLT00owY3ljMLn617YT2B8",
    "authDomain": "nandi-test-b1cb1.firebaseapp.com",
    "databaseURL": "https://nandi-test-b1cb1-default-rtdb.firebaseio.com",
    "projectId": "nandi-test-b1cb1",
    "storageBucket": "nandi-test-b1cb1.appspot.com",
    "messagingSenderId": "745469610293",
    "appId": "1:745469610293:web:d08fb68cdcff345560647c",
    "measurementId": "G-PMFZV50PV6"
}

firebase = pyrebase.initialize_app(firebaseConfig)
pyre_auth = firebase.auth()
pyre_database = firebase.database()
