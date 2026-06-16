# Advanced Setup

## Offline Mode

To have the ESP32-S3 run code automatically after reset or power-on:

1. In Thonny's file panel, open `boot.py` from the `00.1_Boot` folder.
2. Right-click `boot.py` → **Upload to /** to upload it to the MicroPython device root.
3. Right-click your code file (e.g., `HelloWorld.py`) → **Upload to /**.
4. Press the **Reset** button on the ESP32-S3. Your code will execute automatically.

To exit offline mode, click in the Shell panel and press **Ctrl+C**.

---

## Common Thonny Operations

| Task | How |
|------|-----|
| Upload file to ESP32-S3 | Right-click file on computer → **Upload to /** |
| Download file from ESP32-S3 | Right-click file on MicroPython device → **Download to…** |
| Delete file from ESP32-S3 | Right-click file on MicroPython device → **Delete** |
| Create new file | **File** → **New**, write code, then **Save** → **MicroPython device** → name it `main.py` |
| Exit offline mode | Click Shell, press **Ctrl+C** |
