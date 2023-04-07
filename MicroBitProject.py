from microbit import *
import music
import radio
radio.config(group=4)
radio.on()

while True:
    def update():
        mic=microphone.sound_level()
        magne=compass.heading()
        light1=display.read_light_level()
        
        if mic > 75:
            radio.send('Mi')
            sleep(12610)
        elif magne > 285:
            radio.send('Ma')
            sleep(12610)
        elif accelerometer.get_gestures()=='shake':
            radio.send('Sh')
            
    update()
