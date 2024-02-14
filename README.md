# Platformio project for an ESP32 using ESP-IDF

This is a sample project for integrating Memfault with a PlatformIO project using the ESP-IDF framework.

## Setup

1. Install PlatformIO CLI using the instructions [here](https://docs.platformio.org/en/latest//core/installation.html#super-quick-mac-linux).

2. Initialize Memfault submodule:

```bash
git submodule update --init
```

3. Activate the PlatformIO virtual env

```bash
source ~/.platformio/penv/bin/activate
```

4. Install Memfault's dependencies

```bash
pip install -r src/memfault/memfault-firmware-sdk/requirements.txt
pip install memfault-cli
```

## Testing

1. Build with the platformio CLI:
    
```bash
pio run
```
    
2. Upload the symbol file to Memfault:
    
```bash
memfault \
--org-token $MEMFAULT_AUTH_TOKEN \
--org $MEMFAULT_ORG_SLUG \
--project $MEMFAULT_PROJECT_SLUG \
upload-mcu-symbols .pio/build/espidf/firmware.elf
```

3. Flash the device and start the serial monitor

```bash
pio run --target upload --target monitor
```
