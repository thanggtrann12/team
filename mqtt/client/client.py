from paho.mqtt import client as mqtt
broker = "driver.cloudmqtt.com"
port = 18675
client_id = "IAC-Client_blue"
username = "burlgbdf"
password = "0--UiYtSUWAZ"
retain = 1


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(topic, msg):
    client = connect_mqtt()
    ret = client.publish(topic, msg, retain=True)
    if ret[0] == 0:
        return True
    else:
        return False
