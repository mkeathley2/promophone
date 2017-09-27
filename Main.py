import core
from datetime import datetime
from time import sleep

hook = core.hook
lunch_rings = 0
dinner_rings = 0

while True:
    if datetime.now().hour >= 11 and datetime.now().hour < 14:
        Frequency = core.Lunch_Frequency
    else:
        Frequency = core.Default_Frequency

    if hook.is_pressed:
        core.CheckForUpdate()
    while hook.is_pressed:
        core.OffHook()
        break

    if datetime.now().hour in core.lunch_hours and lunch_rings <= 2:
        if core.rand_ring:
            core.Ring()
            lunch_rings += 1

    if datetime.now().hour in core.dinner_hours and dinner_rings <= 2:
        if core.rand_ring:
            core.Ring()
            dinner_rings += 1

    sleep(.5)
