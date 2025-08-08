import time
import pygame

def alarm_in_seconds(seconds, sound_file):
    print(f"Alarm will ring in {seconds} seconds...")
    time.sleep(seconds)
    print("⏰ Alarm ringing now!")

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

delay = int(input("Enter delay in seconds: "))
alarm_in_seconds(delay, "alaram.mp3")  
