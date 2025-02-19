#!/usr/bin/python3
"""
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Définition de la classe qui gère les requêtes HTTP
class MyHandler(BaseHTTPRequestHandler):
    
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
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        # Si la requête est pour /info, retourner les informations sur l'API
        elif self.path == '/info':
            info_data = {"version": "1.0", "description": "A simple API built with http.server"}
            json_info_data = json.dumps(info_data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_info_data.encode('utf-8'))

        # Si l'endpoint n'est pas reconnu, renvoyer une erreur 404
        else:
            self.send_error(404, "Endpoint not found")

# Démarrer le serveur HTTP avec la version flexible
def run(server_class=http.server.HTTPServer, handler_class=MyHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Server running on http://localhost:8000...")
    httpd.serve_forever()

# Lancer le serveur
if __name__ == "__main__":
    run()
