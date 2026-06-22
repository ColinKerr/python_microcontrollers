# Class network

> Adapted from [Python_Tutorial.pdf](../../Python_Tutorial.pdf) — Chapter 28, WiFi Working Modes (Station/STA mode)
>
> Note: Chapter 28 has two reference blocks both labeled "Class network" in the source PDF — one for STA (client) mode, one for [AP mode](../Class_network/AP_Mode.md) — which is why they're grouped together in this folder.

Before each use of `network`, add the statement `import network` to the top of the Python file.

- **`WLAN(interface_id)`**: Sets the WiFi mode.
  - `network.STA_IF`: Client — connects to other WiFi access points.
  - `network.AP_IF`: Access point — allows other WiFi clients to connect.
- **`active(is_active)`**: With a parameter, activates/deactivates the network interface. Without a parameter, queries the current state of the network interface.
- **`scan(ssid, bssid, channel, RSSI, authmode, hidden)`**: Scans for wireless networks available nearby (STA interface only). Returns a tuple list of information about the WiFi access points found.
  - `bssid`: The hardware address of the access point, returned in binary form as a byte object. Use `ubinascii.hexlify()` to convert it to ASCII format.
  - `authmode`: Access type.
    - `AUTH_OPEN = 0`
    - `AUTH_WEP = 1`
    - `AUTH_WPA_PSK = 2`
    - `AUTH_WPA2_PSK = 3`
    - `AUTH_WPA_WPA2_PSK = 4`
    - `AUTH_MAX = 6`
  - `hidden`: Whether to scan for hidden access points.
    - `False`: Only scan for visible access points.
    - `True`: Scan for all access points, including hidden ones.
- **`isconnected()`**: Checks whether the ESP32-S3 is connected to an AP in Station mode. In STA mode, returns `True` if connected to a WiFi access point with a valid IP address; otherwise `False`.
- **`connect(ssid, password)`**: Connects to a wireless network.
  - `ssid`: WiFi name.
  - `password`: WiFi password.
- **`disconnect()`**: Disconnects from the currently connected wireless network.
