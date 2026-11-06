"""Run the Vave HQ on localhost. Standard Python only; no external dependencies."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os, webbrowser, threading
os.chdir(Path(__file__).resolve().parent)
server = ThreadingHTTPServer(('127.0.0.1', 8765), SimpleHTTPRequestHandler)
print('Vave HQ is running at http://127.0.0.1:8765/')
print('Press Ctrl+C to stop the local server.')
threading.Timer(0.7, lambda: webbrowser.open('http://127.0.0.1:8765/')).start()
try: server.serve_forever()
except KeyboardInterrupt: pass
finally: server.server_close()