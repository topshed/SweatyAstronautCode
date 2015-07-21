# Functions for AstroPi Sweaty Astronaut written by Cranmere CodeClub
import time, math, random, logging
from astro_pi import AstroPi
import pygame
import picamera
from pygame.locals import *
import sweaty_astronaut_framed as saf
import RPi.GPIO as GPIO

UP=26
DOWN=13
RIGHT=19
LEFT=20
A=16
B=21
GPIO.setmode(GPIO.BCM)

ap = AstroPi()
ap.set_rotation(270)

def button_pressed(button):
    #written by Richard
	global ap
	global pressed
	#print(button)
	pressed = 1
	
for pin in [UP, DOWN, LEFT, RIGHT, A, B]:
        
    GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=button_pressed, bouncetime=100)

# Logging code by Alfie
tmstmp = time.strftime("%Y%m%d-%H%M%S")
logging.basicConfig(format='%(asctime)s %(message)s',
    filename='Sweaty'+str(tmstmp) +'.log',
                             level=logging.DEBUG)

def write_file(data):
    
    logging.info(data)
    print("writing" + str(data) + ' to file')

def display_prog_start():
    # Written by Reuben
    print("message: starting program")
    

    ap.show_message("program has started",
                   text_colour=[200, 45, 50],
                   back_colour=[200, 120, 50],
                   scroll_speed=0.11)
    
    
def display_baseline():
    # Written by Harry
    ap.show_message("Starting Base-Line",
                    text_colour=[255, 255, 0],
                    back_colour=[0, 0, 255],
                    scroll_speed=0.09)

    ap.show_message("Plese Wait...  ",
                        text_colour=[255, 255, 0],
                        back_colour=[0, 0, 255],
                        scroll_speed=0.09)
    print ("message: recording baseline")

def measure_baseline():
    # written my Harry
    
    print("*** RECORDING BASELINE ***")
    
    base_values = []
    count = 0
    while count < 50:
        
        h = ap.get_humidity()
        base_values.append(h)
        print(h)
        if h > 100:
            
            h = 100.0
        
        display_baseline()
       
        count = count +10
    return(base_values)

    
    

def calc_range(dog):
    #written by epic Dan
    print("calculating range for baseline")
    max_value=max(dog) 
    min_value=min(dog)
    dogs=max_value-min_value
    #print(dogs)
    return dogs
    
    

def calc_mean(dog):
    #written by Epic Dan
    print("calculating mean")
    print(len(dog))
    total =0
    for d in dog:
        total = total + d

    answer = total / len(dog)
    return(answer)
 
    
    

def display_start():
    print("message: starting experiment")

def display_measuring():
    #written by Emily
    print("message: experiment in progress")
    ap.show_message("Do not turn me off!!!!!",text_colour=[0,0,255],back_colour=[255,0,0])

def regular_measuring():
    # written by Harry
    print("measuring")

    h = ap.get_humidity()

    print(h)
    if h > 100:
            
        h = 100.0
        
    write_file('Humidity:  ' + h)
    return(h)
    
    
    

def sweaty_check(Value, Mean, Diff):
#done by octupus ozzy
    answer = (Value-Mean)
    if answer>Diff: 
        return True
    else:
        return False

def display_are_you_there():
    #written by Jappa!!!!!!!!!!
    print("message: are you there?")
    for i in range(8):
        ap.clear(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        time.sleep(0.08)


    ap.show_message('are you there?!',
                scroll_speed=0.0884884884884,
                back_colour=[random.randint(0,145),random.randint(0,145),random.randint(0,145)],
                text_colour=[random.randint(145,255),random.randint(145,255),random.randint(145,255)])

    for i in range(8):
        ap.clear(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        time.sleep(0.08)
    ap.load_image('face8x8.png')           
    time.sleep(0.8)
    ap.show_letter('?',
                   back_colour=[random.randint(0,145),random.randint(0,145),random.randint(0,145)],
                text_colour=[random.randint(145,255),random.randint(145,255),random.randint(145,255)])
    

def display_still_there():
    #written by Freya
    print("message: are you still there? ")
    ap.show_message("are you still there?!", text_colour=[0,255,0],back_colour=[255,0,0])

def display_thankyou():
    # written by Amy H
    ap.show_message("Thank You for experimenting in our test." , text_colour=[246,1,1],back_colour=[45,90,123])
    print("message: thankyou")



def wait_for_joystick(still_there):
    # written by Aaron
    global pressed
    pressed = 0
    print("waiting for joystick")
    pygame.init()
    pygame.display.set_mode((640, 480))
   
    count = 0

    while pressed ==0:
        if count < 10: 
            for event in pygame.event.get():
                
                if event.type == KEYDOWN:
                    
                    if event.key == K_RETURN:
                        ap.show_message("---BUTTON PRESSED---", text_colour=[255,0, 0], back_colour=[0, 0, 0],
                         scroll_speed=0.08)
                   
                        pressed = 1
                        pygame.quit()
        
        #time.sleep(1)
        count = count+1

        if count >= 10: 
            ap.show_message("NOT FOUND :-(", text_colour=[255, 0, 0], back_colour=[0, 0, 0], scroll_speed=0.08)
            pressed = 2
            pygame.quit()
        if still_there:
                display_still_there()
        else:
                display_are_you_there()
        #time.sleep(1)


	
def waiter(there_or_still_there):
    #written by Richard
    global pressed
    pressed = 0
    wait_for_joystick(there_or_still_there)
    if pressed == 1:
        #ap.show_message("Yess!")
        return True
       
    elif pressed == 2:
        #ap.show_message("Nooo!")
       
        return False
    
    
def take_photo():
# written by Alfie and Amy. S
    print("taking photo")
    filename = '/home/pi/Desktop/image.'
    cheese= '.jpg'
    tmstmp = time.strftime("%Y%m%d-%H%M%S")
    with picamera.PiCamera() as cam:
        cam.start_preview()
        time.sleep(2)
        cam.capture(filename+tmstmp+cheese)
        cam.stop_preview()
    return(filename+tmstmp+cheese)
    
    #return('filename')
