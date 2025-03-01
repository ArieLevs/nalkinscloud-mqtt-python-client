# nalkinscloud-mqtt-python-client
[![](https://github.com/arielevs/nalkinscloud-mqtt-python-client/workflows/Python%20package/badge.svg)](https://pypi.org/project/nalkinscloud-mqtt-python-client/)
[![](https://img.shields.io/pypi/v/nalkinscloud-mqtt-python-client.svg)](https://pypi.org/project/nalkinscloud-mqtt-python-client/)
[![](https://img.shields.io/pypi/l/nalkinscloud-mqtt-python-client.svg?colorB=blue)](https://pypi.org/project/nalkinscloud-mqtt-python-client/)
[![](https://img.shields.io/pypi/pyversions/nalkinscloud-mqtt-python-client.svg)](https://pypi.org/project/nalkinscloud-mqtt-python-client/)

MQTT Client package for nalkinscloud project usage

## Usage
```python
## activate package logging by:
# logging.getLogger('nalkinscloud_mqtt_python_client')
from nalkinscloud_mqtt_python_client.devices import SwitchDevice

def set_switch_state(state):
    print("SET SWITCH STATE HERE")
    return state

device = SwitchDevice(set_data_function=set_switch_state)
device.init_broker(broker_host="mosquitto.alpha.nalkins.cloud",
                    broker_port=8883,
                    broker_cert=None,
                    broker_tls=True,
                    broker_tls_skip=True)

# this client will have default 'on_connect' function, but a custom 'on_message' function
device.init_device(device_id='some_device_id', device_type='sensor', device_password='none', qos=0)
device.connect()
device.subscribe("v1/devices/me/rpc/request/+", 1)

# Start the MQTT Mosquito process loop
device.do_loop_forever()
```
