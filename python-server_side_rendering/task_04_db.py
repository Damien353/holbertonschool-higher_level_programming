from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    try:
        with open('products.json', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"JSON Read Error: {e}")
        return None

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
    except (FileNotFoundError, csv.Error, ValueError) as e:
        print(f"CSV Read Error: {e}")
        return None

def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Permet d'accéder aux colonnes par nom
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        
        products = [dict(row) for row in rows]
        return products
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
        return None
    finally:
        conn.close()

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
    else:
        error = "Wrong source"
        return render_template('product_display.html', products=None, error=error)

    if data is None:
        error = "Error reading data"
        return render_template('product_display.html', products=None, error=error)

    # Filtrer par ID si nécessaire
    if product_id is not None:
        data = [item for item in data if item['id'] == product_id]
        if not data:
            error = "Product not found"
            return render_template('product_display.html', products=None, error=error)

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
