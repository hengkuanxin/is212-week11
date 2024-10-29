class OrderProcessor:

    def process_order(self, order):
        self.validate_order(order)
        total_price = self.calculate_total_price(order)
        total_price = self.apply_discount(order, total_price)
        self.update_inventory(order)
        receipt = self.generate_receipt(order, total_price)
        self.send_email(order, receipt)
        return receipt

    def send_email(self, order, receipt):
        print(f"Sending email to customer {order['customer_id']} with receipt:\n{receipt}")

    def generate_receipt(self, order, total_price):
        receipt = f"Customer ID: {order['customer_id']}\n"
        receipt += "Items:\n"
        for item in order["items"]:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${total_price:.2f}\n"
        return receipt

    def update_inventory(self, order):
        for item in order["items"]:
            item_id = item["id"]
            quantity = item["quantity"]
            print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")

    def apply_discount(self, order, total_price):
        discount_rates = {
            "SUMMER20": 0.8,  # 20% discount
            "WELCOME10": 0.9  # 10% discount
        }
        discount_code = order.get("discount_code")
        if discount_code in discount_rates:
            total_price *= discount_rates[discount_code]
        return total_price

    def calculate_total_price(self, order):
        return sum(item["price"] * item["quantity"] for item in order["items"])

    def validate_order(self, order):
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")
