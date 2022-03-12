import pygame
import time
##one way to do it##
#soundfile = "/home/pi/BirdSounds_Raspi/XC165398_Canadian_Goose.wav"

#pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('XC165398_Canadian_Goose.wav')
#clock = pygame.time.Clock()
speaker = sound.play()
while speaker.get_busy():
	time.sleep(5)
##second way to do it##
#pygame.init()
#goose_sound=pygame.mixer.Sound("XC165398_Canadian_Goose.wav")
#pygame.mixer.Sound.play(goose_sound)
