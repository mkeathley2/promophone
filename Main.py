import core
from datetime import datetime
from time import sleep

lunch_rings = 0
dinner_rings = 0

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

    if datetime.now().hour in core.lunch_hours and lunch_rings <= 2:
        if core.rand_ring:
            core.Ring()
            lunch_rings += 1
    # # # RING TEST CODE. DON'T FORGET TO COMMENT OUT
    # if datetime.now().minute in [31, 32]:
    #     core.Ring()

    if datetime.now().hour in core.dinner_hours and dinner_rings <= 2:
        if core.rand_ring:
            core.Ring()
            dinner_rings += 1

    sleep(.5)
