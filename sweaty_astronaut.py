# Main sweaty Astronaut code written by Jasper, comments by Richard
import sweaty_astronaut_framed as saf
from sense_hat import SenseHat
import sweaty_astronaut_functions as swf # where all our functions are defined
import math
import time
import random


saf.load_start_animations()
# Display starting message
swf.display_prog_start()
# Main loop
while True:
    base_values=[ ] # Create empty list for baseline data
    baseline_not_finished = True
    swf.write_file(' start')

    while baseline_not_finished:
        # Stay in this loop until we've got a satisfactory baseline data (range < 2)
        swf.write_file(' baseline start')
        base_values=swf.measure_baseline()
        range_values = swf.calc_range(base_values)
        if range_values<3: # test the range of values
            baseline_not_finished = False
    mean_values=swf.calc_mean(base_values) # calculate the mean value
    swf.write_file('Baseline humidity mean:  ' + str(mean_values) + ' Baseline humidity range: ' + str(range_values) ) # log mean value to file
    swf.display_start()
    no_astro=True#False
    while no_astro:
        # keep doing this until we find an astronaut, then restart this loop 
        swf.display_measuring()
        measured=swf.regular_measuring()
        
        if swf.sweaty_check(measured,mean_values,4): # check for rise in humidity above mean
            swf.write_file(' Possible astronaut')
            swf.display_are_you_there()
             # wait to see if astronaut confirms presence
            if swf.waiter(False):
                swf.write_file('astrothing found:-)') # record our success
                filed=swf.take_photo() # take photo and get filename
                swf.write_file(filed) # log filename of photo to file
                swf.display_thankyou()
            else:
                swf.write_file('astrothing failed:-(') # record that no astronaut confirmed presence
                filed=swf.take_photo() # take photo and get filename
                swf.write_file(filed) # log filename of photo to file
            time.sleep(1) # This is the time between measurements , but we also need to add the display time
            return_to_normal=False
            minute=0
            times=1
            while not return_to_normal:
                   # stick in this loop until humidity base to baseline levels or we give up
                    humid=swf.regular_measuring()
                    print(swf.sweaty_check(humid,mean_values,range_values))
                    if not swf.sweaty_check(humid,mean_values,range_values):
                        return_to_normal=True # humidity is back to normal to restart looking for astronauts
                    else:
                        swf.write_file('Humidity still high')
                        swf.display_still_there() # humidity still high so ask if the astronuat is still there
                        if swf.waiter(True):
                            swf.write_file('astrothing still incoming :-)')
                            saf.sleep_display(times)
                            times=times+1 # wait for longer this time through loop
                        else:
                            minute=minute+1 # humidity high and no sign of astronaut - keep waiting but increment counter
                            
                            saf.sleep_display(10)
                    if minute==10: # if we've been through the loop 10 times, give up and re-measure baseline
                        return_to_normal=True
                        no_astro=False
                        baseline_not_finished=True
                        
        
        
