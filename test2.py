import meshtastic
from pubsub import pub

def onReceive(packet, interface): # called when a packet arrives
    if packet["from"]==476492968:
        message = packet['decoded']['data']['text']
#        print(f"Received: {packet}")
        print(message)
        interface.sendText("RepeaterBot says: " + message)
#    except KeyError:
#        print("Message with no text")

def onConnection(interface, topic=pub.AUTO_TOPIC): # called when we (re)connect to the radio
    # defaults to broadcast, specify a destination ID if you wish
    interface.sendText("hello mesh")

pub.subscribe(onReceive, "meshtastic.receive")
pub.subscribe(onConnection, "meshtastic.connection.established")
# By default will try to find a meshtastic device, otherwise provide a device path like /dev/ttyUSB0
interface = meshtastic.SerialInterface()

