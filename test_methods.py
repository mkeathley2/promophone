import pyaudio

p = pyaudio.PyAudio()



def get_usb_index():
	for i in range(p.get_device_count()):
		if "USB" in p.get_device_info_by_index(i)['name']:
			return p.get_device_info_by_index(i)['index']



