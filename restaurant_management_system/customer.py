class Customer:
    """Represents a customer in the restaurant system."""

    def __init__(self, customer_id, name, phone, orders=None):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.orders = orders or []

    def add_order(self, order_id):
        self.orders.append(order_id)

    def display_info(self):
        return (
            f"Customer ID: {self.customer_id}, Name: {self.name}, "
            f"Phone: {self.phone}, Orders: {len(self.orders)}"
        )

    def get_total_orders(self):
        return len(self.orders)

    def to_file_string(self):
        order_text = "|".join(self.orders)
        return f"{self.customer_id},{self.name},{self.phone},{order_text}"

    @classmethod
    def from_file_string(cls, line):
        parts = line.strip().split(",")
        customer_id = parts[0]
        name = parts[1]
        phone = parts[2]
        orders = parts[3].split("|") if len(parts) > 3 and parts[3] else []
        return cls(customer_id, name, phone, orders)
