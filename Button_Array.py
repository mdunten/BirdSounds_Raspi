# import required libraries
import RPi.GPIO as GPIO
import time
import pygame

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
C6 = 13
C7 = 12

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

def readLine(line, characters):
	GPIO.output(line, GPIO.HIGH)
	if(GPIO.input(C1) == 1):
		print(characters[0])
		playsound(characters[0])
	if(GPIO.input(C2) == 1):
		print(characters[1])
	if(GPIO.input(C3) == 1):
		print(characters[2])
	if(GPIO.input(C4) == 1):
		print(characters[3])
	if(GPIO.input(C5) == 1):
		print(characters[4])
	if(GPIO.input(C6) == 1):
		print(characters[5])
	if(GPIO.input(C7) == 1):
		print(characters[6])
	GPIO.output(line, GPIO.LOW)

def playsound(file):
	pygame.mixer.init()
	sound = pygame.mixer.Sound(file)
	speaker = sound.play()
	#this keep it from exiting before sounds plays
	while speaker.get_busy():
		time.sleep(2)

try:
    while True:
        # call the readLine function for each row of the keypad
        readLine(L1, ["XC165398_Canadian_Goose.wav","A2","A3","A4","A5","A6","A7"])
        readLine(L2, ["B1","B2","B3","B4","B5","B6","B7"])
        readLine(L3, ["C1","C2","C3","C4","C5","C6","C7"])
        #readLine(L4, ["*","0","#","D"])
        time.sleep(0.1)





except KeyboardInterrupt:
    print("\nApplication stopped!")
