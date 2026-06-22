# Class network

> Adapted from [Python_Tutorial.pdf](../../Python_Tutorial.pdf) — Chapter 28, WiFi Working Modes (Access Point/AP mode)
>
> Note: Chapter 28 has two reference blocks both labeled "Class network" in the source PDF — one for [STA mode](../Class_network/STA_Mode.md), one for AP mode — which is why they're grouped together in this folder.

Before each use of `network`, add the statement `import network` to the top of the Python file.

- **`WLAN(interface_id)`**: Sets the WiFi mode.
  - `network.STA_IF`: Client — connects to other WiFi access points.
  - `network.AP_IF`: Access point — allows other WiFi clients to connect.
- **`active(is_active)`**: With a parameter, activates/deactivates the network interface. Without a parameter, queries the current state of the network interface.
- **`isconnected()`**: In AP mode, returns `True` if a station is connected; otherwise `False`.
- **`connect(ssid, password)`**: Connects to a wireless network.
  - `ssid`: WiFi name.
  - `password`: WiFi password.
- **`config(essid, channel)`**: Obtains the MAC address of the access point, or sets the WiFi channel and access point name.
  - `ssid`: WiFi account name.
  - `channel`: WiFi channel.
- **`ifconfig([(ip, subnet, gateway, dns)])`**: Without parameters, returns a 4-tuple `(ip, subnet_mask, gateway, DNS_server)`. With parameters, configures a static IP.
  - `ip`: IP address.
  - `subnet_mask`: Subnet mask.
  - `gateway`: Gateway.
  - `DNS_server`: DNS server.
- **`disconnect()`**: Disconnects from the currently connected wireless network.
- **`status()`**: Returns the current status of the wireless connection.
