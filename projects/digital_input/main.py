from machine import Pin
from utime import sleep

if __name__ == "__main__":
    # NOTE: When following the video it was telling us to use PULL_DOWN and connect the button to power.
    #   This didn't seem to work, and I currently don't understand the difference between PULL_UP and PULL_DOWN, but using PULL_UP and connecting to ground workeds.
    button = Pin(13, mode=Pin.IN, pull=Pin.PULL_UP)

    while True:
        print(button.value())
        sleep(0.1)
