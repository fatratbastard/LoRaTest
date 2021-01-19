import meshtastic
interface = meshtastic.SerialInterface("/dev/ttyUSB0") # By default will try to find a meshtastic device, otherwise provide a device path like /dev/ttyUSB0
interface.sendText("hello ya dozy bastard") # or sendData to send binary data, see documentations for other options.
interface.close()

