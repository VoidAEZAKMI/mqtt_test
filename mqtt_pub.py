import paho.mqtt.client as mqtt


# Определение функции обратного вызова при подключении
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")
    client.publish("sensors/temperature", payload="25.3", qos=0, retain=False)


# Создание экземпляра клиента
client = mqtt.Client(client_id="MQTT_PYTHON_PUBLISHER")

# Установка функции обратного вызова
client.on_connect = on_connect

# Подключение к брокеру
client.connect("localhost", 1883, 60)

# Запуск бесконечного цикла обработки сети
client.loop_forever()
