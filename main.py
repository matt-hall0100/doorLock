from src.dbHandler import getDbLockState, setDbLockState
from src.door import lock, unlock, getPhysicalState

# Get Initial Physical State
lockState = getPhysicalState()

# Main Repeated While Loop
while(True):

    # Database Check
    tmpLockState = getDbLockState()
    if tmpLockState != lockState:
        if tmpLockState:
            lock()
        else:
            unlock()
        lockState = tmpLockState

    # Physical Check
    #tmpPhysicalState = getPhysicalState()
    #if tmpPhysicalState != lockState:
    #    setDbLockState(tmpPhysicalState)
