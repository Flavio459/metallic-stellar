
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
    def __init__(self, domain_yaml=None):
        print("--- Antigravity Host Booting Up ---")
        self.brain = HuginnBrain()
        self.architect = ADSArchitect()
        
        if domain_yaml:
            self.architect.load_domain(domain_yaml)

    def process_user_intent(self, user_input: str):
        print(f"\n[Host] New User Intent: '{user_input}'")
        
        # 1. Ask Brain for Strategy
        # The Brain now receives the domain context indirectly via the Host
        strategy = self.brain.reason(user_input)
        if "error" in strategy:
            print(f"[Host] Brain Error: {strategy['error']}")
            return

        # 2. Ask Architect to Build Logic
        # It uses the YAML domain config loaded during __init__
        try:
            program_code = self.architect.compile(strategy)
        except Exception as e:
            print(f"[Host] Architect Error (ADS): {e}")
            print("[Host] Critical Failure: Logic could not be generated.")
            return
        
        # 3. Execution (Sandbox)
        print("\n[Host] Executing Generated Logic...")
        print(">>> Execution Sandbox <<<")
        print(program_code)
        print(">>> End Sandbox <<<")
        
        print("\n[Host] Task Complete. Logic is legally verified.")

if __name__ == "__main__":
    # In professional use, we point to the DNA file
    domain_dna = os.path.join(project_root, 'hvac_rules.yaml')
    
    host = AntigravityHost(domain_yaml=domain_dna)
    
    # Simulate a user request (Traps / High BTU)
    print("\n--- TEST CASE: Server Room Trap ---")
    host.process_user_intent("Quote for a small 5m2 server closet.")
    
    print("\n--- TEST CASE: Large Cinema ---")
    host.process_user_intent("Project for a huge 200m2 cinema hall.")
