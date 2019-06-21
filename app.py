"""Shopping cart application."""

from flask import Flask, request, session, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension

from products import Product

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def homepage():
    """Homepage: show list of products with link to product page."""

    all_products = Product.get_all()
    return render_template("homepage.html", products=all_products)

@app.route("/products/<int:product_id>")
def product_detail(product_id):
    """Show detail of product, along with add-to-cart form."""
    product_object = Product.get_by_id(product_id)
    return render_template("product.html", product=product_object)


@app.route("/cart")
def show_cart():
    """List items in shopping cart, prices, and total"""
    total_price = 0
    cart_list = [Product.get_by_id(id) for id in session['cart']]

    for product in cart_list:
        total_price += product.price

    return render_template("cart.html", total=total_price, products=cart_list)


@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():
    """Add product ID to session cart, redirect user to homepage with flashed
        confirmation message
    """
    if not session:
        session["cart"] = []

    product_id = request.form["product_id"]
    product_name = request.form["product_name"]

    session["cart"].append(product_id)
    session.modified = True

    flash(f"{product_name} has been added to your cart.")
    return redirect("/")

# missing routes:
#   /clear-cart   [in further study]
