#!/usr/bin/python3
"""
"""

import http.server
import json

# Définition de la classe qui gère les requêtes HTTP
class MyHandler(http.server.BaseHTTPRequestHandler):
    
    # Cette méthode est appelée pour chaque requête GET
    def do_GET(self):
        # Si la requête est pour /data, retourner des données JSON
        if self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode('utf-8'))

        # Si la requête est pour /status, retourner OK
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'OK')  # Réponse "OK"

        # Si la requête est pour la racine, retourner un message de bienvenue
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        # Si l'endpoint n'est pas reconnu, renvoyer une erreur 404
        else:
            self.send_error(404, "Endpoint not found")

# Démarrer le serveur HTTP
def run():
    server_address = ('', 8000)  # Serveur sur le port 8000
    httpd = http.server.HTTPServer(server_address, MyHandler)
    print("Server running on http://localhost:8000...")
    httpd.serve_forever()

# Lancer le serveur
if __name__ == "__main__":
    run()
