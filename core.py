import pygame



def OffHook():

    print("Playing MP3 File...")

    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/test.mp3")
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

    return
