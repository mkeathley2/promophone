import PlayMP3File



from gpiozero import Button

button = Button(2)

while True:
    if button.is_pressed:
        PlayMP3File.play()
    else:
        print("Button is not pressed")
       # PlayMP3File.stop()







# Play MP3 File. I put this code in a module so I can swap out different ways of playing the sound.
#PlayMP3File


