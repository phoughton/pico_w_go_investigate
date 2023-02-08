
# connect to wifi in micropython 
import network
import creds

sta = network.WLAN(network.STA_IF)
if not sta.isconnected():
    sta.active(True)
    sta.connect(creds.WIFI_SSID, creds.WIFI_PASSWORD)
    print("connecting to wifi")
    while not sta.isconnected():
        pass

print("connected to wifi: ", sta.ifconfig())

