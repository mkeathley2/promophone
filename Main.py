import core
from datetime import datetime
from time import sleep

while True:
    if datetime.now().hour >= 11 and datetime.now().hour < 14:
        Frequency = core.Lunch_Frequency
    else:
        Frequency = core.Default_Frequency

    if core.hook.is_pressed:
        core.CheckForUpdate()
    while core.hook.is_pressed:
        core.OffHook()
        break

    # # # RING TEST CODE. DON'T FORGET TO COMMENT OUT
    # if datetime.now().minute in [31, 32]:
    #     core.Ring()

    if datetime.now().minute % Frequency == 0 and datetime.now().second == 10:
        core.Ring()
    sleep(.5)
