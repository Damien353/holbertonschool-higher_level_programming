from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Fonction pour lire le fichier JSON
def read_json():
    try:
        with open('products.json', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"JSON Read Error: {e}")
        return None

# Fonction pour lire le fichier CSV
def read_csv():
    product_list = []
    try:
        with open('products.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                product_list.append(row)
        return product_list
    except FileNotFoundError as e:
        print(f"CSV Read Error: {e}")
        return None
    except csv.Error as e:
        print(f"CSV Parsing Error: {e}")
        return None
    except ValueError as e:
        print(f"Data Type Conversion Error: {e}")
        return None



@app.route('/products')
def products():
    source = request.args.get('source')  # Récupère la source du paramètre de la requête
    id_filter = request.args.get('id', type=int)  # Récupère le paramètre 'id' (si présent)
    products_data = []

    # Vérification de la source (json ou csv)
    if source == 'json':
        products_data = read_json()
    elif source == 'csv':
        products_data = read_csv()
    else:
        error = "Wrong source."  # Si source incorrecte
        return render_template('product_display.html', error=error)

    # Gestion des erreurs de lecture des données
    if products_data is None:
        error = "Error reading product data."
        return render_template('product_display.html', error=error)

    # Filtrage des produits par ID si spécifié
    if id_filter is not None:
        filtered_products = [p for p in products_data if p['id'] == id_filter]
        if not filtered_products:
            error = f"Product with ID {id_filter} not found."
            return render_template('product_display.html', error=error)
        else:
            products_data = filtered_products  # Mise à jour de la liste des produits à afficher

    # Si aucune donnée n'est trouvée ou que la liste est vide
    if not products_data:
        error = "No products available."
        return render_template('product_display.html', error=error)

    # Rendu de la page avec les produits
    return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
