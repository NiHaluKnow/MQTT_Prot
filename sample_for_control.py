import paho.mqtt.client as mqtt

broker = "broker.hivemq.com" 
topic = "buet/cse/2105105/led" # TODO: Put the same topic you used in the ESP code

client = mqtt.Client()
client.connect(broker)

# TODO: the following is an example of publishing a message. You have to modify it so that the python code will run infinitely and wait for input from keyboard. If user presses 'y', it will send "ON"; it will send "OFF" if 'n' is pressed. The program will terminate if user presses 'q'.
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

