import json

import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    # Use set comprehension to collect unique product IDs directly
    product_ids = {
        product_id
        for cart_detail in cart_details
        for product_id in json.loads(cart_detail['contents'])
        if isinstance(json.loads(cart_detail['contents']), list)
    }

    # Fetch product details for unique product IDs
    return [products.get_product(product_id) for product_id in product_ids]

    


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)


