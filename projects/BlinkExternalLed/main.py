from machine import Pin
from utime import sleep
if __name__ == "__main__":

    led = Pin(16, Pin.OUT)

    print("LED starts flashing...")
    while True:
        try:
            led.value(1)
            sleep(1)  # sleep 1sec
            led.value(0)
            sleep(1)  # sleep 1sec
        except KeyboardInterrupt:
            break
    led.off()
    print("Finished.")
