import asyncio
import json
from bluepy.btle import Scanner, DefaultDelegate
import websockets

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

def scan_beacons():
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(5.0)
    beacon_data = []

    for dev in devices:
        for (adtype, desc, value) in dev.getScanData():
            if desc == "Manufacturer":
                beacon_data.append({
                    "mac_address": dev.addr,
                    "rssi": dev.rssi,
                    "manufacturer_data": value
                })
    return beacon_data

async def beacon_server(websocket, path):
    print("Client connected")
    try:
        while True:
            beacon_data = scan_beacons()
            if beacon_data:
                await websocket.send(json.dumps(beacon_data))
            await asyncio.sleep(1)
    except websockets.ConnectionClosed:
        print("Client disconnected")

start_server = websockets.serve(beacon_server, "0.0.0.0", 8000)

print("WebSocket server started on ws://0.0.0.0:8000")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
