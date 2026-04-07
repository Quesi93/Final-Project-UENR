class MenuItem:
    """Represents a food or drink item in the restaurant."""

    def __init__(self, item_id, name, price, category):
        self.item_id = item_id
        self.name = name
        self.price = float(price)
        self.category = category

    def display_info(self):
        return f"{self.item_id} - {self.name} ({self.category}) : GHS {self.price:.2f}"

    def update_price(self, new_price):
        self.price = float(new_price)

    def get_price(self):
        return self.price

    def to_file_string(self):
        return f"{self.item_id},{self.name},{self.price},{self.category}"

    @classmethod
    def from_file_string(cls, line):
        item_id, name, price, category = line.strip().split(",")
        return cls(item_id, name, float(price), category)
