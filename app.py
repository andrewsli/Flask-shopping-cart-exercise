"""Shopping cart application."""

from flask import Flask, request, session, render_template
from flask_debugtoolbar import DebugToolbarExtension

from products import Product

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def homepage():
    """Homepage: show list of products with link to product page."""

    return render_template("homepage.html")

@app.route("/products/<int:product_id>")
def product_detail(product_id):
    """Show detail of product, along with add-to-cart form."""

    return render_template("product.html")

@app.route("/cart")
def show_cart():
    """Show shopping cart."""

    return render_template("cart.html")



# missing routes:
#   /add-to-cart
#   /clear-cart   [in further study]