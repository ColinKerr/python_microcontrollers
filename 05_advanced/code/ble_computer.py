
import asyncio
from bleak import BleakScanner, BleakClient

target_name = "MPY ESP32"

UART_RX_CHAR_UUID="6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
UART_TX_CHAR_UUID="6E400002-B5A3-F393-E0A9-E50E24DCCA9E"


async def handle_rx(_, data):
    print("Received:", data)

async def ainput(prompt: str) -> str:
    return await asyncio.to_thread(input, f'{prompt} ')

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
            text = await ainput("Enter something to send:")

            # Send data to the device
            await client.write_gatt_char(UART_TX_CHAR_UUID.lower(), bytes(text, encoding='ascii'))
            print("Sent:", text)

asyncio.run(main())