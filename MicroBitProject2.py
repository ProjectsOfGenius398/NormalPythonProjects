from microbit import *
import music
import radio
radio.config(group=4)

while True:
        
    message=radio.receive()
    if message == "Mi":
        for i in range(1,5):
            music.play(['d', 'a'])
        music.stop()
        display.scroll('Noise. Noise.')
    elif message == "Ma":
        for i in range(1,5):
            music.play(['d', 'a'])
        music.stop()
        display.scroll('Door. Door')