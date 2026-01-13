
"""
Agentic Engine API Bridge (The Sidecar)
---------------------------------------
Exposes the Antigravity "Army of Agents" as a local HTTP Service.
React/Next.js apps send JSON POST requests here to get verified logic.

Endpoints:
    POST /reason
        Input: {"query": "I need a PMOC for a cinema..."}
        Output: {"result": {...Generated Logic...}, "status": "verified"}
"""

import http.server
import socketserver
import json
import sys
import os

# Ensure we can import our agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.antigravity_host import AntigravityHost

# Initialize the Host ONCE (Cold Start)
print("[Sidecar] Initializing Agent Ecosystem...")
trio_host = AntigravityHost()
print("[Sidecar] Usage: Send POST to http://localhost:8000/reason")

class AgenticHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/reason':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data)
                user_query = data.get('query', '')
                
                print(f"\n[Sidecar] Received Request: {user_query}")
                
                # Hijack stdout to capture the host's print output (since it prints logic)
                # In a real impl, the host would return a dict, but we are capturing the prototype's output.
                from io import StringIO
                old_stdout = sys.stdout
                sys.stdout = mystdout = StringIO()
                
                # RUN THE LOGIC
                trio_host.process_user_intent(user_query)
                
                # Restore stdout
                sys.stdout = old_stdout
                result_log = mystdout.getvalue()
                
                response = {
                    "status": "success",
                    "engine": "Huginn-ADS-Trio",
                    "trace_log": result_log
                }
                
                self._send_json(200, response)
                
            except Exception as e:
                self._send_json(500, {"error": str(e)})
        else:
            self._send_json(404, {"error": "Endpoint not found. Use /reason"})

    def _send_json(self, code, data):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*') # Allow React App
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    # Disable generic logging to keep console clean
    def log_message(self, format, *args):
        pass

PORT = 8000

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), AgenticHandler) as httpd:
        print(f"[Sidecar] Serving Agentic Intelligence on port {PORT}...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[Sidecar] Shutting down...")
