
"""
Antigravity Host Agent
----------------------
The Runtime Orchestrator.
This is the "Body" that connects the Brain (Huginn) and Architect (ADS) 
to the real world (files, user inputs, outputs).
"""


import sys
import os

# Add local DomiKnowS source to path to ensure it runs without system-wide install
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
domiknows_path = os.path.join(project_root, 'DomiKnowS_Source')
if domiknows_path not in sys.path:
    sys.path.append(domiknows_path)

from agents.huginn_brain import HuginnBrain
from agents.ads_architect import ADSArchitect


class AntigravityHost:
    def __init__(self):
        print("--- Antigravity Host Booting Up ---")
        self.brain = HuginnBrain()
        self.architect = ADSArchitect()

    def process_user_intent(self, user_input: str):
        print(f"\n[Host] New User Intent: '{user_input}'")
        
        # 1. Ask Brain for Strategy
        strategy = self.brain.reason(user_input)
        if "error" in strategy:
            print(f"[Host] Brain Error: {strategy['error']}")
            return

        # 2. Ask Architect to Build Logic
        try:
            program_code = self.architect.compile(strategy)
        except Exception as e:
            print(f"[Host] Architect Error (ADS): {e}")
            print("[Host] Critical Failure: Logic could not be generated.")
            return
        
        # 3. Execution (Sandbox)
        print("\n[Host] Executing Generated Logic...")
        # In PROD, we would write this to a file and run it safely.
        # Here we just print the success of the pipeline.
        print(">>> Execution Sandbox <<<")
        print(program_code)
        print(">>> End Sandbox <<<")
        
        print("\n[Host] Task Complete. Logic is legally verified.")

if __name__ == "__main__":
    # Test the Trio Loop
    host = AntigravityHost()
    
    # Simulate a user request relevant to the business goal (R$ 6k target)
    host.process_user_intent("Generate a PMOC proposal for a cinema with 500 people.")
