from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this in production

# Sample products
products = [
    {'id': 1, 'name': 'Laptop', 'price': 999.99, 'description': 'A powerful laptop for work and play.'},
    {'id': 2, 'name': 'Phone', 'price': 599.99, 'description': 'Latest smartphone with great camera.'},
    {'id': 3, 'name': 'Headphones', 'price': 149.99, 'description': 'Noise-cancelling wireless headphones.'},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product.html', product=product)
    return 'Product not found', 404

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart_items = []
    total = 0
    for item_id in session.get('cart', []):
        product = next((p for p in products if p['id'] == item_id), None)
        if product:
            cart_items.append(product)
            total += product['price']
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/checkout')
def checkout():
    # Mock checkout - in real app, integrate payment
    session.pop('cart', None)
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)