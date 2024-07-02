import paho.mqtt.client as mqtt


# Определение функции обратного вызова при подключении
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")
    client.subscribe("sensors/temperature")


# Определение функции обратного вызова при получении сообщения
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")


# Создание экземпляра клиента
client = mqtt.Client(client_id="MQTT_PYTHON_SUBSCRIBER")

# Установка функций обратного вызова
client.on_connect = on_connect
client.on_message = on_message

# Подключение к брокеру
client.connect("localhost", 1883, 60)

# Запуск бесконечного цикла обработки сети
client.loop_forever()
