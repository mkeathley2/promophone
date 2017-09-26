import pygame
import os
import sys
import shutil

import pyaudio

p = pyaudio.PyAudio()



# Varibles

update_file = "PromoPhone.mp3"
promo_file_location = "./"


def OffHook():
    print("Playing MP3 File...")

    pygame.mixer.init()
    pygame.mixer.music.load("PromoPhone.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() is True:
        continue

    print("Done Playing...")

    return


def OnHook():
    print("Stop Playing File...")

    pygame.mixer.music.stop()

    return


def Ring():

    usb_dev_index = get_usb_index()

    print("I'm Ringing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    print("Playing Ring File...")

   # os.system("amixer -c 0 cset numid=" + str(usb_dev_index))
    # os.system("amixer -c 1 set PCM playback 100% unmute")

    pygame.mixer.init()
    pygame.mixer.music.load("Ring.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() is True:
        continue

    print("Done Playing...")


    return


def CheckForUpdate():
    path = "/media/pi/"
    dirs = os.listdir(path)

    for file in dirs:

        update_path = path + file
        print(update_path)

        update_path_full = update_path + update_file

        if os.path.isfile(update_path_full):
            shutil.copy(update_path_full, promo_file_location)
            print("Copied Files Success!!*****@@@@")
        else:
            print("PromoPhone.mp3 not found. Make sure file is on root of flash drive.")

    return


def get_usb_index():
    for i in range(p.get_device_count()):
        if "USB" in p.get_device_info_by_index(i)['name']:
            return p.get_device_info_by_index(i)['index']
