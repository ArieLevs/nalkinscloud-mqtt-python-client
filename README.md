# nalkinscloud-mqtt-python-client
[![](https://github.com/arielevs/pybump/workflows/Python%20package/badge.svg)](https://pypi.org/project/nalkinscloud-mqtt-python-client/)
[![](https://img.shields.io/pypi/v/nalkinscloud-mqtt-python-client.svg)](https://pypi.org/project/nalkinscloud-mqtt-python-client/)
[![](https://img.shields.io/pypi/l/nalkinscloud-mqtt-python-client.svg?colorB=blue)](https://pypi.org/project/nalkinscloud-mqtt-python-client/)
[![](https://img.shields.io/pypi/pyversions/nalkinscloud-mqtt-python-client.svg)](https://pypi.org/project/nalkinscloud-mqtt-python-client/)

MQTT Client package for nalkinscloud project usage

## Usage
```python
## activate package logging by:
# logging.getLogger('nalkinscloud_mqtt_python_client')

from nalkinscloud_mqtt_python_client.mqtt_handler import MQTTClient

client = MQTTClient(broker_host="mosquitto.alpha.nalkins.cloud",
                    broker_port=8883,
                    broker_cert=None,
                    broker_tls=True,
                    broker_tls_skip=True)


# This is the event handler method that receives the Mosquito messages
def on_message(client, userdata, message):
    print("message received: {}".format(message.payload.decode('UTF-8')))

# this client will have default 'on_connect' function, but a custom 'on_message' function
client.init_device(device_id='some_device_id', device_type='sensor', device_password='none',
                   qos=0, subscription_update="status", on_message_func=on_message)
client.connect()
client.subscribe("test_dht_device_id/dht/temperature", 2)
client.subscribe("test_dht_device_id/dht/humidity", 2)

# Start the MQTT Mosquito process loop
client.do_loop_forever()
```
