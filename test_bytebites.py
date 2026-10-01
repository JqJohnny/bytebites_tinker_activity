from models import (
    Category,
    FoodItem,
    Transaction,
    Customer,
    filter_by_category,
    sort_by_popularity,
    calculate_total,
)


def test_filter_by_category():
    burger = FoodItem("Spicy Burger", 8.5, Category.ENTREES, 4.5)
    soda = FoodItem("Large Soda", 2.0, Category.DRINKS, 3.0)
    cake = FoodItem("Cake", 5.0, Category.DESSERT, 4.9)
    items = [burger, soda, cake]

    assert filter_by_category(items, Category.DRINKS) == [soda]


def test_sort_by_popularity():
    burger = FoodItem("Spicy Burger", 8.5, Category.ENTREES, 4.5)
    soda = FoodItem("Large Soda", 2.0, Category.DRINKS, 3.0)
    cake = FoodItem("Cake", 5.0, Category.DESSERT, 4.9)
    items = [burger, soda, cake]

    assert sort_by_popularity(items) == [cake, burger, soda]


def test_calculate_total():
    burger = FoodItem("Spicy Burger", 8.5, Category.ENTREES, 4.5)
    soda = FoodItem("Large Soda", 2.0, Category.DRINKS, 3.0)
    cake = FoodItem("Cake", 5.0, Category.DESSERT, 4.9)
    items = [burger, soda, cake]

    assert calculate_total(items) == 15.5


def test_transaction_calculate_total_matches_module_helper():
    burger = FoodItem("Spicy Burger", 8.5, Category.ENTREES, 4.5)
    soda = FoodItem("Large Soda", 2.0, Category.DRINKS, 3.0)
    items = [burger, soda]
    cust = Customer("Alice", "a@example.com", "555-1234")

    txn = Transaction(cust, items, "credit_card")

    assert txn.calculate_total() == calculate_total(items)


def test_customer_is_verified():
    burger = FoodItem("Spicy Burger", 8.5, Category.ENTREES, 4.5)
    cust = Customer("Alice", "a@example.com", "555-1234")
    txn = Transaction(cust, [burger], "credit_card")

    assert cust.is_verified() is False

    cust.add_purchase(txn)

    assert cust.is_verified() is True
    assert cust.purchase_history == [txn]


if __name__ == "__main__":
    tests = [obj for name, obj in list(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
        print(f"{test.__name__}: passed")
    print(f"\n{len(tests)} tests passed")
