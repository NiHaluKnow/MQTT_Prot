# MQTT LED Control with ESP32 and Python

Control an ESP32 LED over MQTT using a simple Python command-line publisher.

This project demonstrates a basic IoT publish-subscribe workflow:
- ESP32 subscribes to an MQTT topic and toggles LED state.
- Python script publishes `ON` and `OFF` messages from keyboard input.

## Features

- Lightweight MQTT-based LED control
- Works with real ESP32 hardware or Wokwi simulation
- Simple keyboard-driven Python controller
- Uses a public broker for quick testing

## Project Structure

- `sample_for_esp.c`: ESP32 subscriber code (`WiFi` + `PubSubClient`)
- `sample_for_control.py`: Python publisher script (`paho-mqtt`)
- `WOKWI.zip`: Wokwi simulation files
- `IoT Offline.pdf`: assignment/reference material

## MQTT Configuration

- Broker: `broker.hivemq.com`
- Port: `1883`
- Topic: `buet/cse/2105105/led`
- Protocol: MQTT over TCP (no TLS)

Both publisher and subscriber must use the exact same topic.

## How It Works

1. ESP32 connects to Wi-Fi and subscribes to `buet/cse/2105105/led`.
2. Python script waits for user input.
3. Input commands publish messages:
	- `y` publishes `ON`
	- `n` publishes `OFF`
	- `q` exits the script
4. ESP32 receives payload and sets onboard LED:
	- `ON` -> `HIGH`
	- `OFF` -> `LOW`

## Requirements

### ESP32 Side

- ESP32 board or Wokwi ESP32
- Arduino IDE or PlatformIO
- ESP32 core libraries
- `PubSubClient` library

### Python Side

- Python 3.x
- `paho-mqtt`

Install Python dependency:

```bash
pip install paho-mqtt
```

## Running the Project

1. Upload `sample_for_esp.c` to ESP32 (or run in Wokwi).
2. Open Serial Monitor at `115200` baud.
3. Run the Python controller:

```bash
python3 sample_for_control.py
```

4. Enter commands in terminal:
	- `y` to turn LED ON
	- `n` to turn LED OFF
	- `q` to quit

## Troubleshooting

- LED does not change:
	- Confirm both files use the same topic and broker.
	- Check ESP32 Wi-Fi connection in Serial Monitor.
	- Verify broker connectivity (`broker.hivemq.com:1883`).

- Python import error (`No module named paho`):
	- Reinstall package with `pip install paho-mqtt`.

- MQTT message not received:
	- Public brokers can be busy; retry after a short wait.
	- Use a unique topic if collisions occur.

## Future Improvements

- Add authenticated/TLS MQTT broker support
- Add retained messages and QoS handling
- Add status feedback from ESP32 to Python
- Build a web or mobile dashboard for control

## License

This project is licensed under the MIT License. See `LICENSE` for details.
