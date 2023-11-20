import machine
import neopixel
import time

# Define the pin numbers that the PIR sensors are connected to
upper_pir_pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
lower_pir_pin = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)
onboard_led_pin = machine.Pin("LED", machine.Pin.OUT)

# Define the pin number that the NeoPixel LED strip is connected to
neopixel_pin = machine.Pin(2)
num_pixels = 113 # 120 - 7 = 113
pixels = neopixel.NeoPixel(neopixel_pin, num_pixels, bpp=3)

# Define the time for the strip to remain illuminated before turning off again
light_time = 15000

# Define color tuples
LED_off = (0,0,0)
LED_white = (255,255,255)
LED_on = (44,33,20)		# This can be even dimmer but the color is good

# Debounce control
triggered = False

# Turn off the LED strip
def turn_off(timer):
    global triggered
    
    if triggered:
        print("Turning off")
        triggered = False
        pixels.fill(LED_off)
        pixels.write()


# IRQ for the motion sensor at the bottom of the staircase
def lower_motion_detected(pin):
    global triggered
    
    if not triggered:
        print("Lower PIR Sensor")
        triggered = True
        #turn_on_basic()
        turn_on_basic_cascade(rising=True)
        machine.Timer(mode=machine.Timer.ONE_SHOT, period=light_time, callback=turn_off)
    

# IRQ for the motion sensor at the top of the staircase
def upper_motion_detected(pin):
    global triggered
    
    if not triggered:
        print("Upper PIR Sensor")
        triggered = True
        #turn_on_basic()
        turn_on_basic_cascade(rising=False)
        machine.Timer(mode=machine.Timer.ONE_SHOT, period=light_time, callback=turn_off)


# Turn the LED strip on immediately to bright white at a fixed brightness
def turn_on_basic():
    pixels.fill(LED_on)
    pixels.write()


# Turn on the LED strip to bright wihite at a fixed birghtness, one LED at a time from either the top or bottom
def turn_on_basic_cascade(rising=True):
    
    # For a rising cascade, go through the LEDs in order
    start = 0
    end = num_pixels
 
    p = range(start, end)
    if not rising:
        p = reversed(p)
 
    # Set each LED to full white with a tenth of a second delay between each
    for i in p:
        pixels[i] = (LED_on)
        pixels.write()
        time.sleep(0.01)

# Configure the interrupt handler for each sensor
upper_pir_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=upper_motion_detected)
lower_pir_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=lower_motion_detected)


if __name__ == "__main__":    
    # Go into low power mode while waiting for interrupts
    while True:
        
        if onboard_led_pin.value() == 0:
            onboard_led_pin.value(1)
        else:
            onboard_led_pin.value(0)
        
        time.sleep(1)
        #machine.lightsleep(1000)	# Use this for production but it breaks thonny writing. Must wipe flash to use again.
