
"""
Lab Test Runner
---------------
Executes multiple scenarios to validate the "Army of Agents" flexibility.
"""
from agents.antigravity_host import AntigravityHost
import sys

def run_tests():
    print("========================================")
    print("      LAB TESTING: AGENTIC TRIO         ")
    print("========================================")
    
    host = AntigravityHost()
    
    # Scenario 1: Standard Commercial
    print("\n\n>>> TEST CASE 1: Commercial Cinema (Standard Rules) <<<")
    host.process_user_intent("Generate a PMOC proposal for a cinema with 500 people.")
    
    # Scenario 2: Critical Healthcare
    print("\n\n>>> TEST CASE 2: Hospital Surgery Room (Critical Rules) <<<")
    host.process_user_intent("Need HVAC plan for a Hospital Surgery Room to prevent bacteria.")
    
    # Scenario 3: Unknown Domain (Should Fail Gracefully)
    print("\n\n>>> TEST CASE 3: Unknown Domain (Bakery Recipe) <<<")
    host.process_user_intent("How do I bake a cake?")
    
    print("\n\n========================================")
    print("      TESTING COMPLETE                  ")
    print("========================================")

if __name__ == "__main__":
    run_tests()
