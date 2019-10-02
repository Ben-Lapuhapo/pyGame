# Add your Python code here. E.g.
 
# Created by Ben Lapuhapo
# Created on Oct 2019
# Pibadge

import time
import board
import neopixel
# This example shows how to create a single pixel with a specific color channel
# order and blink it.
# Most NeoPixels = neopixel.GRB or neopixel.GRBW
# The 8mm Diffused NeoPixel (PID 1734) = neopixel.RGB


# Configure the setup
PIXEL_PIN = board.NEOPIXEL  # pin that the NeoPixel is connected to
ORDER = neopixel.RGB   # pixel color channel order
COLOR_one= (0, 255, 0) # color to blink
COLOR_two = (255, 0, 0)
CLEAR = (0, 0, 0)      # clear (or second color)
DELAY = 0.25           # blink rate in seconds

# Create the NeoPixel object

pixel = neopixel.NeoPixel(PIXEL_PIN, 5, pixel_order=ORDER)







# Loop forever and blink the color
while True:
    pixel[1] = COLOR_one
    pixel[2] = COLOR_one
    pixel[3] = COLOR_one
    time.sleep(5)
    pixel[3] = CLEAR
    time.sleep(DELAY)
    pixel[3] = COLOR_one
    time.sleep(DELAY)
    pixel[3] = CLEAR
    time.sleep(DELAY)
    pixel[3] = COLOR_one
    time.sleep(DELAY)
    pixel[3] = CLEAR
    time.sleep(DELAY)
    print("2 Lives Left")
    time.sleep(5)
    pixel[2] = CLEAR
    time.sleep(DELAY)
    pixel[2] = COLOR_one
    time.sleep(DELAY)
    pixel[2] = CLEAR
    time.sleep(DELAY)
    pixel[2] = COLOR_one
    time.sleep(DELAY)
    pixel[2] = CLEAR
    time.sleep(DELAY)
    print("1 Life Left")
    time.sleep(DELAY)
    time.sleep(5)
    pixel[1] = COLOR_one
    time.sleep(3)
    print("GAMEOVER")