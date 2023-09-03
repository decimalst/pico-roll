import time
import random
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_P4

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_P4, rotate=0)

display.set_backlight(0.5)
display.set_font("bitmap8")

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
GREEN = display.create_pen(0, 255, 0)

dice = [ 4, 6, 8, 10, 12, 20]
dice_i = 1
num_dice = 1
cur_max = 4


# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()

def rand_int(dice, num_dice): return sum(random.randrange(1, dice+1) for _ in range(num_dice))

def select_dice(dice_i):
    dice_i += 1
    if dice_i >= len(dice):
        dice_i = 0
    cur_max = dice[dice_i]
    return dice_i
# set up
clear()

while True:
    if button_a.read():
        dice_i = select_dice(dice_i)
        cur_max = dice[dice_i]
        clear()
    elif button_b.read():
        if num_dice > 1:
            clear()
            num_dice -= 1
    elif button_x.read():
        clear()
        display.set_pen(WHITE)
        display.text("Rolled {}d{}".format(num_dice,cur_max), 40, 10, 320, 4)
        display.text("Result: {}".format(rand_int(cur_max,num_dice)), 40, 50, 320, 4)
        display.update()
        time.sleep(1)
        clear()
    elif button_y.read():
        if num_dice < 99:
            clear()
            num_dice += 1
    else:
        display.set_pen(GREEN)
        display.text("d{}".format(cur_max), 10, 10, 320, 4)
        display.text("roll".format(cur_max), 250, 10, 320, 4)
        display.text("-".format(num_dice), 10, 180, 320, 4)
        display.text("+".format(num_dice), 300, 180, 320, 4)
        display.text("# of dice = {}".format(num_dice), 60, 210, 320, 4)
        display.update()
    time.sleep(0.0001)

