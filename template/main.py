from machine import Pin
from utime import sleep
from os import listdir

from common import hello_world

if __name__ == "__main__":
    print(listdir("/"))

    print(hello_world())

    pin = Pin("LED", Pin.OUT)

    print("LED starts flashing...")
    while True:
        try:
            pin.toggle()
            sleep(1)  # sleep 1sec
        except KeyboardInterrupt:
            break
    pin.off()
    print("Finished.")
