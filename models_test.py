"""
Designed four classes
Customer class has info about the customer and it links
to transaction through purchase history.

Transaction has a list of items including payment method
and total price.

FoodItem is an indivdual item containing name price an
enumerated category.


Category is an enumerated class containing dessert, drinks,
etc.
"""

from enum import Enum


class Category(Enum):
    DESSERT = "Dessert"
    DRINKS = "Drinks"
    ENTREES = "Entrees"
    APPETIZERS = "Appetizers"
    SNACKS = "Snacks"


class FoodItem:
    def __init__(self, name: str, price: float, category: Category, popularity_rating: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Transaction:
    def __init__(self, customer: "Customer", items: list[FoodItem], payment_method: str):
        self.customer = customer
        self.items = items
        self.payment_method = payment_method

    def calculate_total(self) -> float:
        return sum(item.price for item in self.items)


class Customer:
    def __init__(self, name: str, email: str, phone_number: str, purchase_history: list[Transaction] = None):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.purchase_history = purchase_history if purchase_history is not None else []

    def add_purchase(self, transaction: Transaction) -> None:
        self.purchase_history.append(transaction)

    def is_verified(self) -> bool:
        return bool(self.name) and len(self.purchase_history) > 0