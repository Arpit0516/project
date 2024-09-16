from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Read the references CSV file
references = pd.read_csv('references.csv')

@app.route('/', methods=['GET'])
def index():
    # Read the input CSV file
    input_data = pd.read_csv('input.csv')
    print("Input Data:", input_data.head())  # <--- Add this debug print

    cart = pd.DataFrame()
    for index, row in input_data.iterrows():
        scanner_id = row['Scanner ID']
        print("Scanner ID:", scanner_id)  # <--- Add this debug print
        product = references[references['Scanner ID'] == scanner_id]
        print("Product:", product)  # <--- Add this debug print
        if not product.empty:
            cart = pd.concat([cart, product])
            print("Added product to cart:", product)  # <--- Add this debug print
    print("Cart DataFrame:", cart.head())  # <--- Add this debug print

    # Render the cart.html template with the cart DataFrame
    return render_template('cart.html', product=cart.to_records(index=False))

if __name__ == '__main__':
    app.run(debug=True)