class PaymentReceipt:
    def __init__(self, customer_name, date, amount, payment_method, items):
        self.customer_name = customer_name
        self.date = date
        self.amount = amount
        self.payment_method = payment_method
        self.items = items

    def generate_receipt(self):
        print("Payment Receipt")
        print("----------------")
        print(f"Date: {self.date}")
        print(f"Customer Name: {self.customer_name}")
        print("Items Purchased:")
        for item in self.items:
            print(f"  - {item['name']}: ${item['price']:.2f} x {item['quantity']}")
        print(f"Total Amount: ${self.amount:.2f}")
        print(f"Payment Method: {self.payment_method}")
        print("Thank you for your payment!")

def main():
    customer_name = input("Enter customer name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    items = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        item_price = float(input("Enter item price: "))
        item_quantity = int(input("Enter item quantity: "))
        items.append({'name': item_name, 'price': item_price, 'quantity': item_quantity})
    total_amount = sum(item['price'] * item['quantity'] for item in items)
    payment_method = input("Enter payment method (cash, credit, etc.): ")

    receipt = PaymentReceipt(customer_name, date, total_amount, payment_method, items)
    receipt.generate_receipt()

if __name__ == "__main__":
    main()