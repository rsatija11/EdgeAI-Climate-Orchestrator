import json
from core.edge_inference import ClimateEdgeAI
from core.iot_bridge import IoTBridge

def main():
    print("=========================================")
    print(" ðŸŒ EdgeAI Climate Orchestrator Booting ")
    print("=========================================")
    
    # Initialize hardware bridge and AI inference engine
    bridge = IoTBridge(protocol="SPI")
    ai_engine = ClimateEdgeAI(location="Duke_Engineering_Lab")

    print("\n--- Running Edge Inference Cycle ---")
    results = ai_engine.run_diagnostics()
    
    # Display the processed data (mimicking a dashboard or CRM backend)
    print(json.dumps(results, indent=2))
    print("------------------------------------")

    # Transmit the AI's decision to the physical hardware layer
    bridge.transmit_action(results["ai_prediction"]["action"])

if __name__ == "__main__":
    main()
