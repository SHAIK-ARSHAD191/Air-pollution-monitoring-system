import requests
import time
import random
from datetime import datetime

def generate_sensor_data():
    """Generate random sensor data within realistic ranges"""
    return {
        "location": "Main Office",
        "pm25": random.uniform(5, 35),
        "pm10": random.uniform(10, 50),
        "co2": random.uniform(400, 1500),
        "co": random.uniform(0, 9),
        "temperature": random.uniform(20, 25),
        "humidity": random.uniform(30, 70)
    }

def main():
    """Main function to simulate sensor data"""
    print("Starting sensor simulation...")
    
    while True:
        try:
            data = generate_sensor_data()
            response = requests.post("http://localhost:8000/api/v1/sensor-data/", json=data)
            
            if response.status_code == 200:
                print(f"Data sent successfully at {datetime.now()}")
                print(f"AQI: {response.json()['aqi']}")
            else:
                print(f"Error sending data: {response.status_code}")
                
        except Exception as e:
            print(f"Error: {e}")
            
        # Wait for 30 seconds before sending next reading
        time.sleep(30)

if __name__ == "__main__":
    main() 