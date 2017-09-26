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

    # Mute Right Channel, Turn Left to 100%
    os.system("amixer -c 1 sset PCM,0 100%,0% unmute")

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


    print("I'm Ringing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    print("Playing Ring File...")

   #Mute Left Channel, Turn Right to 100%
    os.system("amixer -c 1 sset PCM,0 0%,100% unmute")

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


