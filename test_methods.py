import pyaudio

p = pyaudio.PyAudio()


def get_usb_index():
	for i in range(p.get_device_count()):
		if "HDMI" in p.get_device_info_by_index(i)['name']:
			return p.get_device_info_by_index(i)['index']

def get_audio_devices():
	for i in range(p.get_device_count()):
		print(p.get_device_info_by_index(i)['name'])


get_audio_devices()

print(get_usb_index())