# ESP32-S3 WROOM Setup — Windows

## 1. Install the CH343 USB Driver

The ESP32-S3 WROOM uses the CH343 chip for USB-to-serial communication. You must install its driver before your computer can communicate with the board.

1. Install driver[CH343SER.EXE](./CH343SER.EXE)
2. Open the folder and double-click **CH343SER.EXE**.
3. Click **INSTALL** and wait for the installation to complete.
4. Close all dialogs.
5. To test
    - Connect the ESP32-S3 WROOM and verify in Device Manager that **USB-Enhanced-SERIAL CH343 (COMx)** now appears under Ports.

---

## 2. Install Thonny IDE

Thonny is the recommended Python IDE for programming the ESP32-S3 with MicroPython.

1. Download the installer: https://github.com/thonny/thonny/releases/download/v5.0.0/thonny-5.0.0-x64.exe
2. Double-click the downloaded `.exe` file.
3. Follow the installer — click **Next** through each step.
4. Optionally change the installation path via **Browse**.
5. Check **Create desktop icon** for easy access later.
6. Click **Install** and wait for completion. Do not click Cancel during installation.
7. Click **Finish**.

---

## 3. Install Python 3

Python 3 must be installed on your computer before you can burn MicroPython firmware to the board.

- Download and install from: https://www.python.org/downloads/
- Follow the official installer instructions. Make sure to check **Add Python to PATH** during installation.

---

## 4. Flash MicroPython Firmware

The ESP32-S3 needs MicroPython firmware flashed onto it before you can run Python programs.

The firmware is located in [setup/Python_Firmware/ESP32_GENERIC_S3-SPIRAM_OCT-20250809-v1.26.0.bin](./Python_Firmware/ESP32_GENERIC_S3-SPIRAM_OCT-20250809-v1.26.0.bin)

![How To connect board via USB](../images/usb_connection.png)

**Flash the firmware:**

1. Connect the ESP32-S3 WROOM to your computer via USB.
    - Use the right hand USB3 connection on the microcontroller
    - If the blue light is blinking when connected press the reset (RST) button
2. Open the folder `setup/Python/Python_Firmware` in File Explorer.
3. Click on the address bar, type `cmd`, and press **Enter** to open a Command Prompt in that folder.
4. Run the following command:
   ```
   python windows.py
   ```
5. Wait for the firmware to finish burning. You will see a completion message when done.

---

## 5. Configure Thonny

1. Open Thonny (use the desktop icon or Start Menu).
2. Go to **View** → enable **Files** and **Shell**.
3. Go to **Run** → **Configure interpreter**.
4. Set the interpreter to **MicroPython (ESP32)**.
5. Set the port to **USB-Enhanced-SERIAL CH343 (COMx)** — the COM number shown in Device Manager.
6. Click **OK**.

---

## 6. Test the Connection

In the **Shell** panel at the bottom of Thonny, type:

```python
print('hello world')
```

Press **Enter**. If `hello world` is printed back, the connection is working correctly.

---

## 7. Running Code

### Run Online (while connected to PC)

1. In Thonny, click **Open…** → **This computer**.
2. Navigate to [01_first_examples/code/HelloWorld.py](../01_first_examples/code/HelloWorld.py)
3. Click **Run current script** (green play button).

> Note: If you press the reset button on the ESP32-S3 while running online, the code will not restart automatically.

