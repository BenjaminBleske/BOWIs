import requests
import json
import http.server
import socketserver



def save_api_result_to_file(filename):
    try:
        response = requests.get('http://worldtimeapi.org/api/ip')
        response.raise_for_status()
        data = response.json()
        
        with open(filename, 'w') as file:
            json.dump(data, file)
        
        print("Die API-Antwort wurde erfolgreich in die Datei", filename, "gespeichert.")
    except requests.exceptions.RequestException as e:
        print("Fehler bei der Anfrage:", e)

save_api_result_to_file('api_result.json')

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

# Port, auf dem der Server lauscht
PORT = 8080

# Erstelle den Server mit dem speziellen Request-Handler
Handler = NoCacheHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print("Server läuft auf Port:", PORT)

# Starte den Server
httpd.serve_forever()



