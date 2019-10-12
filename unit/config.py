import ujson

# Unit - ID
project = "PLACEHOLDER"  # TODO: Fill project name
name = "PLACEHOLDER"  # TODO: Fill unit name - should be unique to the device within one project
mqtt_unit_id = "{}-{}".format(project, name)
unit_id_dict = {"unitID": mqtt_unit_id, "project": project, "name": name}

# Unit - Hardware
# TODO add hardware related configs here, eg. the pins used by the modules

# Unit - Scheduling
gc_collect_interval_sec = 1700
post_status_interval_sec = 600

# WIFI
wifi_ssid = "PLACEHOLDER"  # TODO: Fill wifi access details
wifi_password = "PLACEHOLDER"  # TODO: Fill wifi access details
wifi_connection_check_interval_sec = 1
wifi_ip = "PLACEHOLDER"  # TODO: Fill wifi access details

# MQTT
mqtt_connection_check_interval_sec = 1
mqtt_message_check_interval_ms = 100
mqtt_keepalive_sec = 120
mqtt_qos = 1
mqtt_use_ssl = True
mqtt_queue_size = 10

# MQTT - Credentials
mqtt_server = "PLACEHOLDER"  # TODO: Fill MQTT broker access details
mqtt_port = "PLACEHOLDER"  # TODO: Fill MQTT broker access details
mqtt_user = "PLACEHOLDER"  # TODO: Fill MQTT broker access details
mqtt_password = "PLACEHOLDER"  # TODO: Fill MQTT broker access details

# MQTT - Global topics
mqtt_topic_checkinRequest = "global-checkinrequest"
mqtt_topic_checkin = "global-checkin"
mqtt_topic_checkout = "global-checkout"

# MQTT - topics
mqtt_topic_status_request = "/global/status_request"
mqtt_topic_status = "/global/status"
mqtt_topic_inactive = "/global/inactive"
mqtt_topic_error = "/global/error"
mqtt_topic_control = "/units/{}/control".format(mqtt_unit_id)
mqtt_subscribe_topics = [mqtt_topic_status_request, mqtt_topic_control]



