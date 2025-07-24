#!/usr/bin/env python3
"""
Tesla Stock Prediction Script
Runs the complete pipeline: Reddit scraping -> Model prediction -> Dashboard update
"""

import subprocess
import sys
import os
import socket
import webbrowser
import threading
import http.server
import socketserver
from datetime import datetime

def is_port_in_use(port):
    """Check if a port is already in use"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('localhost', port))
            return False
        except socket.error:
            return True

def start_server(port=8000):
    """Start HTTP server in background thread"""
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"Starting server on http://localhost:{port}")
            httpd.serve_forever()
    except Exception as e:
        print(f"Server error: {e}")

def run_prediction():
    """Run the Tesla prediction pipeline"""
    print("Starting Tesla Stock Prediction Pipeline...")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    # Change to parent directory (main project folder)
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_dir)
    print(f"Working from: {project_dir}")
    
    try:
        # Run the prediction notebook
        print("Running prediction notebook...")
        result = subprocess.run([
            "jupyter", "nbconvert", "--to", "notebook", 
            "--execute", "predict_tesla.ipynb",
            "--output", "predict_tesla_executed.ipynb"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Prediction completed successfully!")
            print("Results saved to data/latest_prediction.json")
            print("Dashboard updated - refresh your browser!")
            
            # Check if prediction file exists
            if os.path.exists("data/latest_prediction.json"):
                print("Prediction file created successfully")
            else:
                print("Warning: Prediction file not found")
        else:
            print("Error running prediction:")
            print(result.stderr)
            return False
            
        # Clean up temporary files
        try:
            os.remove("predict_tesla_executed.ipynb")
            print("Cleaned up temporary files")
        except:
            pass
            
    except FileNotFoundError:
            print("Error running prediction:")
            print(result.stderr)
            return False
            
    except FileNotFoundError:
        print("Jupyter not found. Install with: pip install jupyter")
        print("Alternative: Run the cells in predict_tesla.ipynb manually")
        return False
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
        
    print("="*60)
    print("Pipeline completed!")
    
    # Start server and open browser
    port = 8000
    dashboard_url = f"http://localhost:{port}/output/tesla_dashboard.html"
    
    if is_port_in_use(port):
        print(f"Server already running on port {port}")
    else:
        print(f"Starting HTTP server on port {port}...")
        server_thread = threading.Thread(target=start_server, args=(port,), daemon=True)
        server_thread.start()
        # Give server a moment to start
        import time
        time.sleep(1)
    
    print(f"Opening dashboard: {dashboard_url}")
    webbrowser.open(dashboard_url)
    
    if not is_port_in_use(port):
        print("Keep this terminal open to maintain the server!")
        print("   Press Ctrl+C to stop the server")
        try:
            # Keep main thread alive if we started the server
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nServer stopped by user")
    
    return True

if __name__ == "__main__":
    success = run_prediction()
    sys.exit(0 if success else 1)
