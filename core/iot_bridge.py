class IoTBridge:
    """
    Acts as the communication middleware between the Edge AI software 
    and the underlying hardware peripherals (HVAC, alarms, GSM modules).
    """
    def __init__(self, protocol="I2C"):
        self.protocol = protocol
        print(f"[HARDWARE INIT] IoT Bridge established via {self.protocol} protocol.")

    def transmit_action(self, action_code):
        """Translates the AI model's output into hardware-level execution."""
        if action_code == "TRIGGER_HVAC_AND_ALERT":
            print(f"[{self.protocol} TX] ðŸš¨ ANOMALY DETECTED. Activating cooling subsystems and sending GSM alert.")
        elif action_code == "MAINTAIN_STATE":
            print(f"[{self.protocol} TX] âœ… Climate stable. Holding current hardware state.")
        else:
            print(f"[{self.protocol} TX] Unknown action code: {action_code}")
