#!/usr/bin/python3
"""
"""
import requests
import csv

def fetch_and_print_posts():
    # Envoyer une requête GET
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    # Vérifier le code de statut
    print(f"Status Code: {response.status_code}")
    
    # Si la requête a réussi, traiter la réponse
    if response.status_code == 200:
        posts = response.json()  # Convertir la réponse en JSON
        for post in posts:
            print(post["title"])  # Afficher les titres des posts

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()  # Convertir la réponse en JSON
        
        # Préparer les données à écrire dans le CSV
        posts_data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        
        # Écrire dans un fichier CSV
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()  # Écrire l'en-tête
            writer.writerows(posts_data)  # Écrire les données des posts