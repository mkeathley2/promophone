import core
import random
from datetime import datetime
from gpiozero import Button



Default_Frequency = 60
Lunch_Frequency = 15

hook = Button(2)




while True:
    if datetime.now().hour >= 11 and datetime.now().hour < 14:
        Frequency = Lunch_Frequency
    else:
        Frequency = Default_Frequency

    if hook.is_pressed:
        core.CheckForUpdate()
        core.OffHook()
    if datetime.now().minute % Frequency == 0 and datetime.now().second == 10:
        core.Ring()



"""
count = 0
iterations = 48
iter = 0

while iter <= iterations:
    r_int = int(random.randrange(0,100))
    if r_int % 8 == 0 and r_int != 0:
        print(r_int)
        count += 1
    iter += 1
print(count)
"""
