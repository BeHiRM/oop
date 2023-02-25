
class Item:
    pay_rate = 0.8  # the pay rafter after 20% discont

    def __init__(self, name: str, price: float, quantity: int):
        assert price > 0, f"price {price} is not greater than zero!"
        assert quantity > 0, f"Quantity {quantity} is not greater than zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_totla_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate


item1 = Item("phone", 100, 5)
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 5)
item2.has_numpad = True
item2.pay_rate = 0.7
print(Item.__dict__)
print(Item.pay_rate, item1.pay_rate, item2.pay_rate)
print(item1.name, item1.price, item1.quantity,
      item1.calculate_totla_price())
print(item2.name, item2.price, item2.quantity,
      item2.calculate_totla_price())
