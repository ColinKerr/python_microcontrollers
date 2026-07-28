# This example demonstrates a UART periperhal.

import bluetooth
from ble_peripheral import BLEBasePeripheral


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
