#!/usr/bin/env python2

import paho.mqtt.client as mqtt
import urllib

#Conf Enclosure Plugin Output ID
out_1 = "1"
out_2 = "2"

#Conf Octo Print
op_api = "00000000000000000000000000000000"
op_ip = "192.168.8.120"

#Conf MQTT broker
broker_ip = "192.168.8.150"
broker_port = 1883
broker_timeout = 60
topic_sub = "gBridge/u000/octopi/#"
topic_out1 = "gBridge/u000/octopi/led"
topic_out2 = "gBridge/u000/octopi/printer"

def main():
   def on_connect(client, userdata, flags, rc):
	client.subscribe(topic_sub)
   def on_message(client, userdata, msg):
	if msg.topic == topic_out1 :
		if msg.payload == "1" :
			url = "http://{0}/plugin/enclosure/setIO?status=true&index_id={1}&apikey={2}".format(op_ip, out_1, op_api)
			htmlfile=urllib.urlopen(url)
			htmltext=htmlfile.read()
			#print "OUT 1 ON"
		if msg.payload == "0" :
			url = "http://{0}/plugin/enclosure/setIO?status=false&index_id={1}&apikey={2}".format(op_ip, out_1, op_api)
			htmlfile=urllib.urlopen(url)
			htmltext=htmlfile.read()
			#print "OUT 1 OFF"
	if msg.topic == topic_out2 :
		if msg.payload == "1" :
			url = "http://{0}/plugin/enclosure/setIO?status=true&index_id={1}&apikey={2}".format(op_ip, out_2, op_api)
			htmlfile=urllib.urlopen(url)
			htmltext=htmlfile.read()
			#print "OUT 2 ON"
		if msg.payload == "0" :
			url = "http://{0}/plugin/enclosure/setIO?status=false&index_id={1}&apikey={2}".format(op_ip, out_2, op_api)
			htmlfile=urllib.urlopen(url)
			htmltext=htmlfile.read()
			#print "OUT 2 OFF"
	
   client = mqtt.Client()
   client.on_connect = on_connect
   client.on_message = on_message

   client.connect(broker_ip, broker_port, broker_timeout)

   client.loop_forever()

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      pass
