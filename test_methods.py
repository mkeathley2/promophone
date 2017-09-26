import pyaudio

p = pyaudio.PyAudio()

usb_dev = 0

for i in range(p.get_device_count()):
	if "USB" in p.get_device_info_by_index(i)['name']:
		usb_dev = p.get_device_info_by_index(i)['index']

print(usb_dev)