# import required libraries
import RPi.GPIO as GPIO
import time
import pygame
import os

# these GPIO pins are connected to the keypad
# change these according to your connections!
L1 = 4
L2 = 3
L3 = 2
#L4 = 1

C1 = 10
C2 = 9
C3 = 7
C4 = 8
C5 = 11
C6 = 12
C7 = 13

# Initialize the GPIO pins

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
#GPIO.setup(L4, GPIO.OUT)

# Make sure to configure the input pins to use the internal pull-down resistors

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# The readLine function implements the procedure discussed in the article
# It sends out a single pulse to one of the rows of the keypad
# and then checks each column for changes
# If it detects a change, the user pressed the button that connects the given line
# to the detected column

##Get Sound Files From /home/pi/Desktop/SoundBoard/Sounds
def list_full_path(directory):
        return [os.path.join(directory,file) for file in os.listdir(directory)]

arr_files = list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row1/1")
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row1/2")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row1/3")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row1/4")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row1/5")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row1/6")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row1/7")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row2/1")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row2/2")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row2/3")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row2/4")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row2/5")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row2/6")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row2/7")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row3/1")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row3/2")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row3/3")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row3/4")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row3/5")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row3/6")[0])
arr_files.append(list_full_path("/home/pi/Desktop/SoundBoard/Sounds/Row3/7")[0])

##

def readLine(line, characters):
	GPIO.output(line, GPIO.HIGH)
	if(GPIO.input(C1) == 1):
		print(characters[0])
		playsound(characters[0])
	if(GPIO.input(C2) == 1):
		print(characters[1])
		playsound(characters[1])
	if(GPIO.input(C3) == 1):
		print(characters[2])
		playsound(characters[2])
	if(GPIO.input(C4) == 1):
		print(characters[3])
		playsound(characters[3])
	if(GPIO.input(C5) == 1):
		print(characters[4])
		playsound(characters[4])
	if(GPIO.input(C6) == 1):
		print(characters[5])
		playsound(characters[5])
	if(GPIO.input(C7) == 1):
		print(characters[6])
		playsound(characters[6])
	GPIO.output(line, GPIO.LOW)

def playsound(file):
	pygame.mixer.init()
	print(arr_files[file])
	sound = pygame.mixer.Sound(arr_files[file])
	#hardcoding sounds to only play for 5 seconds, remove if not needed 
	speaker = sound.play(loops=0,maxtime=3000,fade_ms=1)
	#this keep it from exiting before sounds plays
	while speaker.get_busy():
		time.sleep(2)

try:
    while True:
        # call the readLine function for each row of the keypad
        readLine(L1, [0,1,2,3,4,5,6])
        readLine(L2, [7,8,9,10,11,12,13])
        readLine(L3, [14,15,16,17,18,19,20])
        #readLine(L4, ["*","0","#","D"])
        time.sleep(0.1)





except KeyboardInterrupt:
    print("\nApplication stopped!")
