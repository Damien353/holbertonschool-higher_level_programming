from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception as e:
        print(f"JSON Read Error: {e}")
        return []

def read_csv():
    products = []
    try:
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert price to float and id to int
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        print(f"CSV Read Error: {e}")
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    id_filter = request.args.get('id', type=int)

    if source == 'json':
        products_data = read_json()
    elif source == 'csv':
        products_data = read_csv()
    else:
        error = "Wrong source. Use 'json' or 'csv'."
        return render_template('product_display.html', error=error)

    # Filter by ID if provided
    if id_filter is not None:
        products_data = [p for p in products_data if p['id'] == id_filter]
        if not products_data:
            error = f"Product with ID {id_filter} not found."
            return render_template('product_display.html', error=error)

    return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
