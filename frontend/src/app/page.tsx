"use client"
import { useEffect, useState } from 'react';

export default function Home() {
  const [beacons, setBeacons] = useState([]);

  useEffect(() => {

    const socket = new WebSocket('ws://localhost:8000'); // バックエンドの WebSocket サーバー URL
  
    socket.onopen = () => {
      console.log('WebSocket connection established');
    };
  
    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log(data);  // 受信データをコンソールに表示
      setBeacons(data);
    };
  
    socket.onclose = () => {
      console.log('WebSocket closed');
    };
  
    socket.onerror = (error) => {
      console.log('WebSocket error: ', error);
    };
  
    return () => {
      socket.close();
    };
  }, []);
  

  
  return (
    <div>
      <h1>iBeacon Data</h1>
      <ul>
        {beacons.map((beacon, index) => (
          <li key={index}>
            <strong>MAC:</strong> {beacon.mac_address}, <strong>RSSI:</strong> {beacon.rssi}, <strong>Data:</strong> {beacon.manufacturer_data}
          </li>
        ))}
      </ul>
    </div>
  );
}
