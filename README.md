# MQTT LED Control (ESP32 + Python)

This project demonstrates basic MQTT communication between:
- an ESP32 client that subscribes to LED control messages, and
- a Python script that publishes LED commands from keyboard input.

The LED state on ESP32 is controlled by messages sent from the Python program(sample_for_control.py)

## Project Files

- `sample_for_esp.c`: ESP32 MQTT subscriber code (turns LED ON/OFF).
- `sample_for_control.py`: Python MQTT publisher code (sends ON/OFF).

## MQTT Broker

- Broker host: `broker.hivemq.com`
- Port: `1883`
- Protocol: MQTT over TCP (no TLS in this demo)
- Authentication: none (public broker)

This project uses a public broker for easy testing. Because it is shared, messages may be delayed occasionally and topic collisions are possible if someone else uses the same topic.

For a production setup, use a private broker with authentication and TLS.

## How It Works

- Python sends:
  - `ON` when you press `y`
  - `OFF` when you press `n`
  - exits when you press `q`
- ESP32 listens to the topic and:
  - sets LED pin HIGH for `ON`
  - sets LED pin LOW for `OFF`

## Requirements

### ESP32 Side

- ESP32 board (or Wokwi ESP32 simulation)
- Arduino IDE or PlatformIO
- Libraries:
  - `WiFi` (ESP32 core)
  - `PubSubClient`

### Python Side

- Python 3.x
- `paho-mqtt`

Install Python dependency:

```bash
pip install paho-mqtt
```

## Run Instructions

1. Flash/upload the ESP32 code from `sample_for_esp.c`.
2. Open Serial Monitor (baud: `115200`) to view connection and messages.
3. Run the Python controller:

```bash
python3 sample_for_control.py
```

4. Use keyboard input in Python terminal:
   - `y` -> publish `ON`
   - `n` -> publish `OFF`
   - `q` -> quit

## Notes

- MQTT broker used: `broker.hivemq.com` (public broker).
- Public brokers may occasionally be busy or rate-limited.
- Keep internet connection active for both sides.

## Troubleshooting

- No LED response:
  - Verify both files use the exact same topic.
  - Check ESP32 is connected to Wi-Fi.
  - Confirm MQTT broker and port (`1883`).
- Python script fails to import mqtt:
  - Reinstall dependency: `pip install paho-mqtt`
- ESP32 not connecting in Wokwi:
  - Keep SSID/password as configured in the code for Wokwi guest network.
