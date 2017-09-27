import random

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



# def get_usb_index():
# 	for i in range(p.get_device_count()):
# 		if "HDMI" in p.get_device_info_by_index(i)['name']:
# 			return p.get_device_info_by_index(i)['index']
#
# def get_audio_devices():
# 	for i in range(p.get_device_count()):
# 		print(p.get_device_info_by_index(i)['name'])
#
#
# get_audio_devices()
#
# print(get_usb_index())