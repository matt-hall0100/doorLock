import firebase_admin
from firebase_admin import credentials, db


cred = credentials.Certificate('./res/accountKey.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://door-unlock-db303.firebaseio.com'})
ref = db.reference('lock_state')


## setDbLockState()
#  @brief Sets the inputted state to the database lock state
#  @param Value to set databases state
def setDbLockState(state):
    ref.set(state)


## getDbLockState()
#  @brief Gets the database lock state
#  @return Value of databases state
def getDbLockState():
    return ref.get()
