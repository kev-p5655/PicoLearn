# PicoLearn
Small Projects for Pico 2

## Connect USB using WSL
REF: https://learn.microsoft.com/en-us/windows/wsl/connect-usb
- usbipd list
- usbipd bind --busid 3-13
- usbipd attach --wsl --busid 3-13
NOTE: Need to run the last command everytime the device is reconnected.