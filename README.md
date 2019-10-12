# IoT MCU Modules

## Summary
- Part of the [tlvlp IoT project](https://github.com/tlvlp/iot-project-summary)
- Template for the MCU side API of the services

## Usage
Upload helper scrips can be found at [micropython-upload](https://github.com/tlvlp/micropython-upload) but they still need some manual configuration.

A working implementation can be found at the [iot-mcu-bazsalikon-soil](https://github.com/tlvlp/iot-mcu-bazsalikon-soil) repository to serve as a guide.

1. Clone this repository or otherwise use it as a temple for your own project
2. Select already implemented modules from the modules folder or create
module wrapper classes of your own hardware modules based on the existing ones
3. Fill the placeholder values in the [config.py](unit/config.py) marked with TODO comments (highlighted in PyCharm)
4. Fill in the module related sections in the [unit_service.py](unit/unit_service.py) marked with TODO comments (highlighted in PyCharm)
5. Update the ESP32 module to the latest [MicroPython](http://micropython.org/download#esp32) firmware.
6. Upload the contents to the MCU with eg. [ampy](https://github.com/scientifichackers/ampy) that is also used by the above scripts.
7. Make sure that the MQTT broker that is part of the tlvlp IoT project is running.
8. Test the unit with either via the project or via any third party MQTT client by subscribing and posting to theAPI topics.
9. The unit is ready to be installed.

## Implementing your own hardware modules
- **Values**: Modules accept and return values that must be convertible to float/double
- **Retrieve values**: Modules should expose a function that returns their current status in a touple of (moduleID, value)
- **Async**: Should idealy use the uasyncio library and return control when possible, especially for reading slower modules
- **Controllable**: Most modules are read only (sensors) but for those that can be controlled:
    - Should expose a method that returns their moduleID for routing the incoming requests to the right module
    - Should expose a method that handles the incoming value change
    - Currently only doubles/floats can be used on the server side!
    - eg. the [relay](modules/relay.py) module

# MCU API
- Below you can find the API that each Unit has to implement in order to work with the server side of the project.
The skeleton project in this repository already supports it.
- On the ser MQTT topics are inherited from the project's [deployment repository](https://gitlab.com/tlvlp/iot.server.deployment) via environment variables.
- All MQTT messages must be in JSON format.

## Server side topics

### Global Status Request
|||
| :--- | :--- |
| Topic | /global/status_request |
| Environment variable | MCU_MQTT_TOPIC_GLOBAL_STATUS_REQUEST |
| Description | Requests a status update from all subscribed MCUs, who must respond by sending a status update to the global status topic |
| Who publishes here? | Server side |
| Who subscirbes here? | All MCUs |

Payload format:
>The payload is ignored, an empty string is recommended.
```
""
```

### Global Inactive
|||
| :--- | :--- |
| Topic | /global/inactive |
| Environment variable | MCU_MQTT_TOPIC_GLOBAL_ERROR |
| Description | All MCU set a "last will" when they connect to the MQTT broker containing their unitID details as the payload.  |
|| The broker sends the unit's payload after a pre-set time of inactivity.  |
|| The Unit whose details are sent to this topic will be flagged as inactive. |
| Who publishes here? | MQTT broker on behalf of the MCUs |
| Who subscirbes here? | Server side |

Payload format:
```json
{
    "unitID": "tlvlp.iot.BazsalikON-soil", 
    "project": "tlvlp.iot.BazsalikON", 
    "name": "soil"
}
```

### Unit control topics
|||
| :--- | :--- |
| Topic | Each topic is unit-specific |
| Environment variable | No related variable |
| Description | All MCUs have their unit-specific topic generated in this pattern: "/units/**unitID**/control" |
| Who publishes here? | Server side |
| Who subscirbes here? | Each MCU to their own topic |

Payload format:
>Each  message should contain *only one* Module's details!
```json
{
    "relay|growlight": 1
}
```


## MCU side topics

### Global Status
|||
| :--- | :--- |
| Topic | /global/status |
| Environment variable | MCU_MQTT_TOPIC_GLOBAL_STATUS |
| Description |  All MCU send their status messages to this topic.  |
|| Modules use a "module_reference\|module_name" format where the module_reference is matched to its Module on the server side |
|| and the module_name is used to distinguish different instances of the module within a given Unit (eg. multiple relays) |
| Who publishes here? | All MCUs |
| Who subscirbes here? | Server side |
Payload format:
```json
{
    "unitID": "tlvlp.iot.BazsalikON-soil", 
    "project": "tlvlp.iot.BazsalikON", 
    "name": "soil", 
    "relay|growlight": 0, 
    "gl5528|lightPercent": 85, 
    "somo|soilMoisturePercent": 80
}
```

### Global Error
|||
| :--- | :--- |
| Topic | /global/error |
| Environment variable | MCU_MQTT_TOPIC_GLOBAL_ERROR |
| Description | All MCU send their error messages to this topic. |
| | For obvious reasons the connection related errors cannot be posted here.|
| Who publishes here? | All MCUs |
| Who subscirbes here? | Server side |
Payload format:
```json
{
    "unitID": "tlvlp.iot.BazsalikON-soil", 
    "project": "tlvlp.iot.BazsalikON", 
    "name": "soil", 
    "error": "Error! Something mildly terrible has happened."
}
```