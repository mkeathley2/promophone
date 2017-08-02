import pygame



def play():

    print("Playing MP3 File...")

    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/test.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() is True:
        is
        continue

    print("Done Playing...")

    return

def stop():
    print("Stop Playing File...")

    pygame.mixer.music.stop()

    return


