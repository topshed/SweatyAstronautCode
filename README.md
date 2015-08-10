##AstroPi Sweaty Astronaut Code

You can read more about this project and the design and coding process [here] (http://richardhayler.blogspot.co.uk/2015/07/writing-our-astro-pi-sweaty-astronaut.html). 

The project consists of three .py files:

**sweaty_astronaut.py** - the main code loop
**sweaty_astronaut_functions.py** - contains all the functions used by the main program loop
**sweaty_astronaut_framed.py** - A collection sof animation lists used at various points in the code

There is also **face8x8.png** which is a static image loaded at one point.

###Dependencies

The following Python libraries need to be installed and imported:

astro_pi

math

random

logging

pygame

picamera

RPi.GPIO


XXX include flowchart ***

### Usage

Make sure you have your AstroPi HAT and a Pi camera installed.

Then run:

sudo python sweaty_astronaut.py
 
###List of functions

Any function that starts with the *display_* will be used to write a (hopefully) helpful message to the LED matrix, normally to describe what is going on. Almost all of these functions are defined in **sweaty_astronaut_functions.py**

####button_pressed(button)

Checks to see if one of the GPIO []flight case] (https://www.raspberrypi.org/blog/astro-pi-flight-case/) buttons has been pressed. This code is lifted from []here] (https://www.raspberrypi.org/learning/astro-pi-guide/inputs-outputs/buttons.md). Sets the variable *pressed* to 1 if a button press is detected.

####write_file(data)

Takes the string passed in as data and writes it to the file (using the Python logging library) 

####display_prog_start()

Announces that the program has started.

####display_baseline()

Announces that measuring the baseline humidity is about to start.

####measure_baseline()

Takes a series of humidity values and returns them as a list.

####calc_range(dog)

Takes a list of values and returns their range (max - min) 

####calc_mean(dog)

Takes a list of values and returns their mean 

####display_start()

Announces that the main part of the experiment has started.

####display_measuring()

Announces that the program is running and warns that the Pi should not be turned off.

####regular_measuring()

Takes a humidity measurement, writes it to our log file, and then returns it.

####sweaty_check(value, mean, diff)

Compares the *value* to the *mean* and returns True if the difference is greater than *diff*.

####display_are_you_there()

Uses the LED to ask if there is someone there - this function is triggered if the humidity reading rises. Tries to attract the astronaut's attention using flashing colours and an image.

####display_still_there()

Asks if the astronaut is still there. Displayed after a humidity rise, if the value does not return to the baseline range.

####display_thakyou()

if an astronaut presses either the joystick on one of the flight case buttons, this message is shown.

####wait_for_joystick()

Waits a certain amount of time for the joystick to be pressed. Displays a success message if it is pressed and a failure notification if is isn't. Changes the value of the global variable *pressed* if (you guessed it) the joystick is pressed. 

While it waits it will run either *display_are_you_there()* or *display_still_there()* depending on if *still_there* is True or False

####waiter(there_or_still_there)

Handles the responses of *wait_for_joystick()* and *button_pressed()*. If the variable *pressed* is equal to 1 when *wait_for_joystick()* completes, it returns True.

####take_photo()

Uses the camera to take a photo, writing the filename (based on date/time) to the log file. 

**Other functions in sweaty_astronaut_framed.py:**

####load_start_animations()

Runs through all the animations in this file and shows them on the LED matrix. The time between each frame of the animation is set according to how long that sequence is (number of frames).

####sleep_display(breaks)

If we have some waiting time during execution of the main program, instead of sleeping with a blank LED matrix, show an animation with frames/second scaled to fit the desired sleep time (breaks).
### Optimisation

The following values should be tweaked to allow for operational conditions:

In sweaty_astronaut_functions, Line 75, in *measure_baseline()*: if more than 5 humidity values are needed to establish a baseline, invrement this value by 10 for each additional reading required. 

In sweaty_astronaut_functions, Lines 196 & 211, in *wait_for_joystick()*: If more time is needed for the astronaut to press the button/joystick confirming their presence, make the value of count in these conditionals bigger (seconds)

In sweaty_astronaut, Line 24: the value in this conditional for range_values is how much natural variation in humidty (i.e. the baseline) we tolerate. Make this value higher if you want to allow a greater fluctuation. You may need to the also adjust the value below. 

In sweaty_astronaut, Line 35: the final value passed to *sweaty_check()* is the change in humidity that will indicate the possible presence of an astronaut and trigger the code segment that waits for a button confirmation. Chnage this value if it is too sensitive or not sensitive enough.  

In sweaty_astronaut, Line 69: The value in this conditional determines how long we wait after a possible astronaut event for te humidity to return to baseline value before we give up and re-calculate the baseline.