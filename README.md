# Soundmeter to MQTT

The script provides the decibel readings of a sound meter to the MQTT server.

On the hardware side it requires one of these meters:

https://www.amazon.com/gp/product/B00ABCKI7W/ref=oh_aui_search_detailpage?ie=UTF8&psc=1

The meters are typically only capable of reading 2 values a second. So no audio recording.

## Installation

Install:

- python
- pyusb
- paho.mqtt for python
