import paho.mqtt.client as mqtt

broker = "broker.hivemq.com" 
topic = "buet/cse/2105105/led" # Put the same topic you used in the ESP code

client = mqtt.Client()
client.connect(broker)

# this loop will run until the user decides to quit by pressing 'q' and will publish "ON" or "OFF" to the MQTT topic based on user input , which will control the LED connected to the ESP device subscribed to the same topic.(topic: buet/cse/2105105/led)
while True:
	key = input("Press y for ON, n for OFF, q to quit: ").strip().lower()
	if key == "y":
		client.publish(topic, "ON")
		print("Published: ON")
	elif key == "n":
		client.publish(topic, "OFF")
		print("Published: OFF")
	elif key == "q":
		break
	else:
		print("Invalid input. Use y, n, or q.")

client.disconnect()


