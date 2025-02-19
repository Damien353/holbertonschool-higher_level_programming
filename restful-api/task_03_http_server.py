#!/usr/bin/python3
"""
"""

import http.server
import json

# Classe de gestion des requêtes HTTP
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Si la requête est pour /data, retourner des données JSON
        if self.path == '/data':
            # Créer un dictionnaire Python
            data = {"name": "John", "age": 30, "city": "New York"}
            # Convertir en JSON
            json_data = json.dumps(data)

            # Envoi de la réponse 200 (OK)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')  # Type de contenu JSON
            self.end_headers()  # Fin des en-têtes
            self.wfile.write(json_data.encode('utf-8'))  # Envoi des données JSON

        # Si la requête est pour /status, retourner OK
        elif self.path == '/status':
            # Envoi de la réponse 200 (OK)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')  # Type de contenu texte
            self.end_headers()  # Fin des en-têtes
            self.wfile.write(b'OK')  # Réponse "OK"

        # Si l'endpoint n'est pas reconnu, renvoyer une erreur 404
        else:
            self.send_error(404, "Endpoint not found")  # Code d'erreur 404

# Fonction pour démarrer le serveur
def run(server_class=http.server.HTTPServer, handler_class=MyHandler):
    server_address = ('', 8000)  # Serveur écoutant sur le port 8000
    httpd = server_class(server_address, handler_class)
    print('Server running on http://localhost:8000...')
    httpd.serve_forever()  # Lancer le serveur et attendre les requêtes

# Point d'entrée du script
if __name__ == '__main__':
    run()  # Démarrer le serveur
