import os
import pygame

os.system("export AUDIODEV=hdmi:0,0")
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('PromoPhone.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
	pygame.time.Clock().tick(10)

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