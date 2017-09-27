import core
from datetime import datetime
from time import sleep

while True:
    c_time = datetime.now()

    if c_time.hour <= 9 or c_time.hour >= 22:
        sleep(3600)

    if c_time.hour >= 11 and c_time.hour < 14:
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

    if c_time.minute % Frequency == 0 and c_time.second == 10:
        core.Ring()
    sleep(.5)
