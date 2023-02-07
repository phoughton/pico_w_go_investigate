
# connect to wifi in micropython 
import network

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("TP-Link_BF88", "55702461")
   
# outpiut wifi status
print(sta.isconnected())

