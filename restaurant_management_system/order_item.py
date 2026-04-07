class OrderItem:
    """Represents one menu item inside an order."""

    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = int(quantity)
        self.price = float(price)

    def calculate_subtotal(self):
        return self.quantity * self.price

    def update_quantity(self, quantity):
        self.quantity = int(quantity)

    def display_info(self):
        return (
            f"{self.name} x {self.quantity} @ GHS {self.price:.2f} "
            f"= GHS {self.calculate_subtotal():.2f}"
        )

    def to_file_string(self):
        return f"{self.item_id};{self.name};{self.quantity};{self.price}"

    @classmethod
    def from_file_string(cls, text):
        item_id, name, quantity, price = text.split(";")
        return cls(item_id, name, int(quantity), float(price))
