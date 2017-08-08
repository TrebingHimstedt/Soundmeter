import sys
import usb.core
import usb.util
import time
import random
import paho.mqtt.publish as publish

# init values
lastValue = 0

# access the usb device
dev = usb.core.find(idVendor=0x16c0, idProduct=0x5dc)
assert dev is not None

# run forever
while True:
        try:
                # read the value from the device
                ret = dev.ctrl_transfer(0xC0, 4, 0, 0, 200)
                # calculate the real value
                dB = (ret[0] + ((ret[1] & 3) * 256)) * 0.1 + 30

                # only report changes
                if (str(lastValue)!=str(dB)):
                        print str(lastValue)+" - "+ str(dB)

                        lastValue=dB
                        print "publishing to MQTT"
                        publish.single("/sensor/sound", str(dB), hostname="localhost")
                        print "published"
        except Exception as e:
                # we will ignore errors as we want to run forever
                print(e)
                print 'error'
                pass