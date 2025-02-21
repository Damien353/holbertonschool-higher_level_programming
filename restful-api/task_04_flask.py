#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire des utilisateurs en mémoire
users = {}

# Route racine
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Route /data : Retourne la liste des utilisateurs
@app.route("/data")
def data():
    return jsonify(list(users.keys()))

# Route /status : Retourne OK
@app.route("/status")
def status():
    return "OK"

# Route dynamique /users/<username> : Retourne un utilisateur spécifique
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        user["username"] = username
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route /add_user : Accepte une requête POST pour ajouter un utilisateur
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    # Vérifier si l'username est présent dans les données
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    # Ajouter l'utilisateur dans le dictionnaire
    users[data["username"]] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    # Retourner la confirmation avec les détails de l'utilisateur ajouté
    return jsonify({
        "message": "User added",
        "user": users[data["username"]]
    }), 201

# Lancer l'application si ce fichier est exécuté directement

if __name__ == "__main__":
    app.run()