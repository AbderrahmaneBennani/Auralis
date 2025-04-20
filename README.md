# Auralis 🔊🏠

**Auralis** is a voice-controlled smart home assistant designed to run on a Raspberry Pi. It integrates local speech recognition with Zigbee-based device control, enabling seamless interaction with your smart devices — completely offline.

Auralis is still a work in progress. It originally used whisper.cpp for speech-to-text, but Whisper was too slow and heavy for the Raspberry Pi. I switched to Picovoice for lightweight, offline wake word detection and intent recognition, which works much better on low-power hardware.

---

## 🛠 Hardware Used

- **Raspberry Pi 4B**
- **Sonoff Zigbee 3.0 USB Dongle Plus-E**
- **IKEA TRÅDFRI Zigbee Lightbulb**
- **SteelSeries Arctis Nova 7** (for microphone input)
- **Standard Bluetooth Speaker**

---

## 🚀 Features

- 🐦 Wake word detection using [Picovoice Porcupine](https://picovoice.ai/platform/porcupine/)
- 🧠 Intent recognition with [Picovoice Rhino](https://picovoice.ai/platform/rhino/)
- 💡 Zigbee device control using [Zigbee2MQTT](https://www.zigbee2mqtt.io/)
- 🔐 Fully offline — no cloud required
- 🛜 MQTT integration for smart home messaging

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone git@github.com:AbderrahmaneBennani/Auralis.git
cd Auralis
```

### 2. Set up Python environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Environment Variables

Make sure to create a `.env` file in the root directory with your Picovoice API key: 

```bash
PICO_API_KEY=your_key_here
```

### 4. Install Zigbee2MQTT

Follow the official [Zigbee2MQTT installation guide](https://www.zigbee2mqtt.io/guide/installation/01_linux.html) for your platform.

Make sure your Sonoff USB Dongle E is recognized and configured.

Start Zigbee2MQTT with:

```bash
sudo systemctl start zigbee2mqtt
```

And enable on boot:

```bash
sudo systemctl enable zigbee2mqtt
```

## 🗣 Usage

After setting up everything, run the main assistant script:

```bash
python main.py
```

Speak into the mic and Auralis will interpret your commands to control Zigbee devices.

---

## ➕ Extending Auralis

Adding new Zigbee devices and voice commands is easy!

### 🧩 Adding Zigbee Devices

Once your new Zigbee device is powered on and in pairing mode, Zigbee2MQTT will automatically detect it. You can:

1. View connected devices in the Zigbee2MQTT dashboard.
2. Use the device ID in your ExecuteCommand logic to trigger specific actions.

### 🎤 Changing the Wake Word

To change the Wake Word, you only need to change the Python/Custom_Data/Custom_Keyword.ppn file.
You can generate your own from the [Picovoice Console](https://console.picovoice.ai/).

### 🗣️ Adding Voice Commands (Rhino Intents)

To add or modify voice commands:

1. Edit the [`Yaml/rhino_model.yaml`](Yaml/rhino_model.yaml) file to include new intents and slots.
2. Upload the YAML to [Picovoice Console](https://console.picovoice.ai/) to generate a new `.rhn` model.
3. Replace the existing model file (`Yaml/rhino_model.rhn`) with your new one.
4. Update your command-handling logic to reflect the new intents.

## ☕ Support

If you find this project useful and want to support continued development:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-donate-yellow?logo=buy-me-a-coffee&style=for-the-badge)](https://www.buymeacoffee.com/revcodes)

---

## 📄 License

MIT License © 2025 Abderrahmane Bennani
