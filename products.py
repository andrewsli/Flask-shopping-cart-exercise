"""Database of products.

In a real project, we'd use a real database here, so that products could
be dynamically added and deleted. For the purpose of this exercise, we won't
need to add/change/delete products, so this fake-database-in-simple-Python
will do nicely.
"""

class Product():
    """Purchasable item in our store.

    You can add a product:

        >>> p = Product.add("Tea cup", "A lovely cup", "http://image.com", 5)

    It will get an auto-assigned id:

        >>> p.id
        1

    You can retrieve a product by id:

        >>> Product.get_by_id(1)
        <Product id=1 name="Tea cup">

    You can get all products, in id order:

        >>> Product.get_all()
        [<Product id=1 name="Tea cup">]
    """

    _products = []

    def __init__(self, id, name, description, image, price):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.price = price

    def __repr__(self):
        return f"""<Product id={self.id} name="{self.name}">"""

    @classmethod
    def add(cls, name, description, image, price):
        """Add a new product, adding to our product list."""

        new_id = len(cls._products) + 1
        new_product = cls(new_id, name, description, image, price)
        cls._products.append(new_product)
        return new_product

    @classmethod
    def get_by_id(cls, id):
        """Retrieve a product by ID."""

        return cls._products[int(id) - 1]

    @classmethod
    def get_all(cls):
        """Return list of all products."""

        return cls._products


Product.add(
    name="Tea cup",
    description="Empire Bone Pearl China Tea Cup",
    image="/static/1.jpeg",
    price=54,
)

Product.add(
    name="Gutenberg Bible",
    description="Very early printing of the Vulgate, ca 1450. Limited quantity available.",
    image="/static/2.jpeg",
    price=10000000,
)

Product.add(
    name="Rubber band",
    description="Stretchy, red, and very useful",
    image="/static/3.jpeg",
    price=0.20,
)

