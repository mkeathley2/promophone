import random

import pygame
import os
import shutil

from gpiozero import Button

pygame.init()

# Varibles
audio_file = "PromoPhone.mp3"
promo_file_location = "./"
hook = Button(2)
Default_Frequency = 60
Lunch_Frequency = 15
lunch_hours = [11, 12, 13, 14]
dinner_hours = [18, 19, 20]

# Lower the ring chance variable to increase likelihood of ring
ring_chance = 25



def OffHook():
    print("Playing MP3 File...")

    # Mute Right Channel, Turn Left to 100%
    os.system("amixer -c 1 sset PCM,0 100%,0% unmute")

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        if hook.is_pressed:
            pygame.time.Clock().tick(10)
        else:
            OnHook()
            break

    print("Done Playing...")

    return


def OnHook():
    print("Stop Playing File...")

    pygame.mixer.music.stop()

    return


def Ring():


    print("I'm Ringing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    print("Playing Ring File...")

   # Mute Left Channel, Turn Right to 100%
    os.system("amixer -c 1 sset PCM,0 0%,100% unmute")

    pygame.mixer.init()
    pygame.mixer.music.load("Ring.mp3")

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        if hook.is_pressed:
            break

    print("Done Playing...")


    return


def CheckForUpdate():
    path = "/media/pi/"
    dirs = os.listdir(path)

    for directory in dirs:

        update_path = path + directory
        print(update_path)

        update_path_full = update_path + '/' + audio_file

        if os.path.isfile(update_path_full):
            try:
                shutil.copy(update_path_full, promo_file_location)

                print("Copied Files Success!!*****@@@@")
                play_update_success()
                return
            except:
                play_missing_file_error()
        else:

            print("PromoPhone.mp3 not found. Make sure file is on root of flash drive.")
            continue

    # play_missing_file_error()
    return


def play_update_success():
    pygame.mixer.init()
    pygame.mixer.music.load("UpdateSuccess.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        if hook.is_pressed:
            pygame.time.Clock().tick(10)
        else:
            OnHook()
            break


def play_missing_file_error():
    pygame.mixer.init()
    pygame.mixer.music.load("UpdateError.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        if hook.is_pressed:
            pygame.time.Clock().tick(10)
        else:
            OnHook()
            break


def rand_ring():
    r_int = int(random.randrange(0, 100))
    if r_int % ring_chance == 0 and r_int != 0:
        return True
    else:
        return False
