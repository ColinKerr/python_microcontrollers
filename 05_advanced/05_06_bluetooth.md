# Bluetooth Connection

Bluetooth is a handy way to send data between the ESP32-S3 and a computer or phone.  In this project the ESP32-S3 will act as a bluetooth device and the computer will connect to it.  Once a connection is made data can be set between the two in either direction.

## New Concepts

- BleakClient python bluetooth library
- asynchronous code

### BleakClient

[BleakClient](https://bleak.readthedocs.io/en/latest/api/client.html) is a cross platform python bluetooth library.  It must be installed on the computer that will connect to the microcontroller.

> Note: The ESP32-S3 has it's own bluetooth client library: https://docs.micropython.org/en/v1.26.0/library/bluetooth.html


### Asynchronous Code

Asynchronous code is helpful when communicating over a network because the response to a request may take a very long time to come.  We will avoid digging into details here but the basics are straight forwards.

- Functions that may take a long time get marked with the `async` keyword

  `async def myFunction()`
- Functions that are marked with the `async` keyword must be awaited to hold the program up until the function completes

  `await myFunction()`

The end result is that code executes the same as normal, linearly from top to bottom, but the computer knows that other code can execute while it is awaiting for a function to return.

## Component List

- ESP32-S3 microcontroller
- A computer with bluetooth and python installed.

## Circuit

This project has no circuit


## Code

### Microcontroller Code

**File:** [05_advanced/code/ble_micro.py](./code/ble_micro.py)

This code is very long so only excerpts will be shown here.  Also the module 'ble_advertising' will not be covered but it is used here.

```python
def demo():
    ble = bluetooth.BLE()
    p = BLEBasePeripheral(ble)

    def on_rx(rx_data):
        print("\nRX", rx_data)

    p.on_write(on_rx)
    
    print("Please connect to ESP32S3.")

    while True:
        if p.is_connected():
            # Short burst of queued notifications.
            tx_data = input("Enter anything: ")
            print("Send: ", tx_data)
            p.send(tx_data)


if __name__ == "__main__":
    demo()
```

This code will setup the microcontroller as a bluetooth device available for a computer to connect to.  It will listen for data sent from the computer and print it and it will send any data input into the console back to the computer.


### Computer Code

**File:** [05_advanced/code/ble_computer.py](./code/ble_computer.py)

```python
import asyncio
from bleak import BleakScanner, BleakClient

target_name = "ESP32S3"

UART_RX_CHAR_UUID="6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
UART_TX_CHAR_UUID="6E400002-B5A3-F393-E0A9-E50E24DCCA9E"


async def handle_rx(_, data):
    print("Received:", data)

async def main():
    address = ""
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)
        if d.name == target_name:
            print("Found microcontroller:", d)
            address = d.address

    if address == "":
        print ("Failed to find device with name: ", target_name)
        return
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")

        # Start notifications for receiving data
        await client.start_notify(UART_RX_CHAR_UUID.lower(), handle_rx)

        while True:
            text = input("Enter something to send:")

            # Send data to the device
            await client.write_gatt_char(UART_TX_CHAR_UUID.lower(), bytes(text, encoding='ascii'))
            print("Sent:", text)

asyncio.run(main())
```

This code connects to the bluetooth device named 'ESP32S3'.  It will print any data sent from the bluetooth device and send any data entered on the computer to the bluetooth device.

> Note: The computer must have python3, bluetooth enabled and the 'bleak' module installed.

## How to run

### Microcontroller
1. Open Thonny → `05_advanced/code/`.
2. Right-click `ble_advertising.py` → **Upload to /** — wait for it to finish uploading to the ESP32-S3.
2. Double-click `ble_micro.py`.
3. Click **Run current script**.

### Computer
1. In the terminal navigate to `05_advanced/code/`.
2. Run the following command `python3 ble_computer.py`

If the code fails to run saying the 'bleak' module cannot be found install it using this command then run again:

```bash
pip3 install bleak
```

> NOTE: If the computer fails to find the microcontroller the name might be wrong.  Look at the list of found devices listed by the computer and find the most likely name.  Update `ble_computer.py` `target_name` variable to use this name and try again.