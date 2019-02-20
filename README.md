# OctoPrint-Enclosure-Relay-MQTT-Integration

Easy script to make a possibility to Turn ON and OFF Relays added in OctoPrint Enclosure Plugin with MQTT. 
Can be easliy used with gbridge.io and then with Google Home Assistant.

## Instalation

1. Download ```mqtt_enclosure_plugin.py``` to your ```/home/pi/``` folder.
2. Change Config parameters to your variables.
```
out_1,out_2 - id of relays can be found in settings of enclosure plugin in octoprint
op_api - api of octoprint 
op_ip - ip of octoprint
broker_ip, broker_port, broker_timeout - information of your MQTT broker eg. Mosquitto
topic_sub - main topic to subscribe
topic_out1, topic_out2 - topics for your relays
```
3. Change perrmision ```chmod +x mqtt_enclosure_plugin.py```
4. Run in background ```nohup /home/pi/mqtt_enclosure_plugin.py &```

## If you want to use it with gbridge.io and Google Home:

0. Create account on: http://gbridge.io

1. Install Mosquito newest version on your RPI: https://theembeddedlab.com/tutorials/install-mosquitto-on-a-raspberry-pi/

2. Edit ```sudo nano /etc/mosquitto/mosquitto.conf``` adding at the end:
```
connection gbridge-io
address mqtt.gbridge.io:8883
bridge_attempt_unsubscribe true
bridge_protocol_version mqttv311
cleansession true
remote_username {gbridge-mqtt-username}
remote_password {gbridge-mqtt-password}
remote_clientid gbridge-u{userid}-{randomstring}
topic gBridge/u{uid}/octopi/+ both 0 "" ""
bridge_capath /etc/ssl/certs/
bridge_tls_version tlsv1.2
```
3. Restart broker 
```sudo /etc/init.d/mosquitto restart```
3. Add Device on: https://gbridge.kappelt.net/device
```
Device type: Outlet
Traits: On and Off
Action Topic: gBridge/u{uid}/octopi/printer
Status Topic: gBridge/u{uid}/octopi/printer
```
4. Add and autorize Kabbelt gBridge account in Google Home Assistant.
