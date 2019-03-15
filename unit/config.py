import ujson

# Unit - ID
module = "PLACEHOLDER"
project = "PLACEHOLDER"
name = "PLACEHOLDER"
unit_id_dict = {"module": module, "project": project, "name": name}


# WIFI
wifi_ssid = "PLACEHOLDER"
wifi_password = "PLACEHOLDER"
wifi_connection_check_interval_sec = 1
wifi_ip = "PLACEHOLDER"

# MQTT
mqtt_connection_check_interval_sec = 1
mqtt_message_check_interval_ms = 100
mqtt_keepalive_sec = 120
mqtt_qos = 1
mqtt_use_ssl = True
mqtt_queue_size = 10

# MQTT - Credentials
mqtt_server = "PLACEHOLDER"
mqtt_port = "PLACEHOLDER"
mqtt_user = "PLACEHOLDER"
mqtt_password = "PLACEHOLDER"

# MQTT - Global topics
mqtt_topic_checkinRequest = "global-checkinrequest"
mqtt_topic_checkin = "global-checkin"
mqtt_topic_checkout = "global-checkout"

# MQTT - Unit topics
mqtt_unit_id = "{}-{}-{}".format(module, project, name)
mqtt_checkout_payload = ujson.dumps(unit_id_dict)
mqtt_subscribe_topics = [mqtt_topic_checkinRequest]



