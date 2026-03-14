import random

class ClimateEdgeAI:
    """
    Simulates an Edge AI model deployed on a Raspberry Pi or PIC Microcontroller.
    Processes live I2C/SPI sensor data to predict climate anomalies.
    """
    def __init__(self, location="Central_Warehouse_Alpha"):
        self.location = location
        self.thresholds = {"temp_max": 32.0, "co2_max": 600.0}

    def read_sensors(self):
        """Simulates raw data ingestion from MQ-series and DHT sensors via I2C/SPI."""
        return {
            "temperature_c": round(random.uniform(22.0, 36.0), 2),
            "humidity_percent": round(random.uniform(40.0, 85.0), 2),
            "co2_ppm": round(random.uniform(350, 750), 2)
        }

    def predict_anomaly(self, sensor_data):
        """
        Runs localized inference to detect climate risks without cloud latency.
        (Simulates a lightweight neural network or decision tree)
        """
        risk_score = (sensor_data["temperature_c"] * 0.5) + (sensor_data["co2_ppm"] * 0.05)
        
        is_anomalous = (
            sensor_data["temperature_c"] > self.thresholds["temp_max"] or 
            sensor_data["co2_ppm"] > self.thresholds["co2_max"]
        )
        
        return {
            "risk_score": round(risk_score, 2),
            "anomaly_detected": is_anomalous,
            "action": "TRIGGER_HVAC_AND_ALERT" if is_anomalous else "MAINTAIN_STATE"
        }

    def run_diagnostics(self):
        data = self.read_sensors()
        prediction = self.predict_anomaly(data)
        return {"sensor_data": data, "ai_prediction": prediction}
