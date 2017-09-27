import core
from datetime import datetime
from time import sleep

lunch_rings = 0
lunch_ring_max = 200

dinner_rings = 0
dinner_ring_max = 2

last_ring = 0

while True:
    c_time = datetime.now()

    if c_time.hour <= 9 or c_time.hour >= 22:
        sleep(3600)

    # if c_time.hour >= 11 and c_time.hour < 14:
    #     Frequency = core.Lunch_Frequency
    # else:
    #     Frequency = core.Default_Frequency

    if core.hook.is_pressed:
        core.CheckForUpdate()
    while core.hook.is_pressed:
        core.OffHook()
        break

    if c_time.hour in core.lunch_hours and lunch_rings <= lunch_ring_max:
        if core.rand_ring() and c_time.hour != last_ring:
            core.Ring()
            lunch_rings += 1
            # last_ring = c_time.hour
            core.Ring()

    # # # RING TEST CODE. DON'T FORGET TO COMMENT OUT
    # if datetime.now().minute in [31, 32]:
    #     core.Ring()

    if c_time.hour in core.dinner_hours and dinner_rings <= dinner_ring_max:
        if core.rand_ring() and c_time.hour != last_ring:
            core.Ring()
            dinner_rings += 1
            last_ring = c_time.hour
            core.Ring()

    sleep(.5)
