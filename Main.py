import core
from datetime import datetime
from time import sleep


hook = core.hook

while True:
    if datetime.now().hour >= 11 and datetime.now().hour < 14:
        Frequency = core.Lunch_Frequency
    else:
        Frequency = core.Default_Frequency

    if hook.is_pressed:
        core.CheckForUpdate()
    while hook.is_pressed:
        core.OffHook()

	if datetime.now().minute in [28,29,30,31]:
		core.Ring()
    if datetime.now().minute % Frequency == 0 and datetime.now().second == 10:
        core.Ring()
    sleep(.5)
