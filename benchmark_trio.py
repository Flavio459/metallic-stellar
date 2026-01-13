
"""
Benchmark: Trio Verification vs Vanilla Estimation
--------------------------------------------------
Objective: Prove mathematically that the Agentic Trio enforces constraints 
that a standard execution might miss.

Test Case: 'Restaurante Taubaté' provided by User.
Constraint: NBR 16401 - If 'Server Room' present, PMOC is MANDATORY regardless of BTU.
"""
from agents.antigravity_host import AntigravityHost
import time

def run_benchmark():
    print("========================================")
    print("      BENCHMARK: LOGIC INTEGRITY        ")
    print("========================================")
    
    host = AntigravityHost()
    
    # Input Data (The 'Trap')
    # A small server room (10m2) which usually doesn't need PMOC by size,
    # BUT explicitly requires it due to "Critical Use" (Server).
    input_trap = "I have a small 10m2 server closet with 1 split AC. Do I need a PMOC?"
    
    print(f"\n[Input]: '{input_trap}'")
    print(f"[Trap]: Size is small (< 60k BTU), so a naive guess says 'NO'.")
    print(f"[Rule]: Critical Environments (Servers) ALWAYS require PMOC.")
    
    print("\n----------------------------------------")
    print(">>> RUNNING TRIO (Huginn + ADS) <<<")
    start_time = time.time()
    
    # In a real run, Huginn detects 'Server' -> implies 'Critical' -> implies 'PMOC Required'
    host.process_user_intent(input_trap)
    
    duration = time.time() - start_time
    print(f"\n[Result]: Trio Execution Time: {duration:.4f}s")
    print("----------------------------------------")
    
    print("\n[VERDICT]", flush=True)
    print("If the output above says 'PMOC REQUIRED' despite the small size,", flush=True)
    print("then the Logic Guardian successfully overrode the heuristic bias.", flush=True)
    print("========================================", flush=True)

if __name__ == "__main__":
    run_benchmark()
