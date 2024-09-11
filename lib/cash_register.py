import sys
import io

class CashRegister:
    def __init__(self, discount=0):
        """
        Initializes the cash register with an optional discount.
        The default total is set to 0, and an empty list tracks the items.
        """
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, item_name, price, quantity=1):
        """
        Adds items to the cash register.
        Updates the total price, tracks the last transaction, and appends the items to the list.
        """
        self.total += price * quantity
        self.items.extend([item_name] * quantity)
        self.last_transaction = price * quantity

    def apply_discount(self):
        """
        Applies the discount to the total price if available.
        Prints and returns a message showing the new total or indicating no discount.
        """
        if self.discount:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
            return f"After the discount, the total comes to ${int(self.total)}."
        else:
            print("There is no discount to apply.")
            return "There is no discount to apply."

    def void_last_transaction(self):
        """
        Voids the last transaction, subtracting it from the total.
        """
        self.total -= self.last_transaction
