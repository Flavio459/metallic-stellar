
"""
Simulates the React Application calling the Sidecar API.
"""
import urllib.request
import json
import time
import sys

def test_bridge():
    url = "http://localhost:8000/reason"
    payload = {
        "query": "Integration Test: Hospital PMOC request from React App"
    }
    
    print(f"[Client] Connecting to {url}...")
    print(f"[Client] Sending Payload: {payload}")
    
    req = urllib.request.Request(
        url, 
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        # Retry logic in case server is still booting
        for i in range(5):
            try:
                with urllib.request.urlopen(req) as response:
                    print("\n[Client] Success! Server Responded:", flush=True)
                    print(f"HTTP Status: {response.status}", flush=True)
                    body = response.read().decode('utf-8')
                    parsed = json.loads(body)
                    print(json.dumps(parsed, indent=2), flush=True)
                    return
            except Exception as e:
                print(f"[Client] Connection attempt {i+1} failed ({e}). Retrying in 1s...", flush=True)
                time.sleep(1)
                
        print("[Client] Critical Failure: Could not connect to Sidecar API.", flush=True)
        
    except Exception as e:
        print(f"[Client] Error: {e}", flush=True)

if __name__ == "__main__":
    test_bridge()
