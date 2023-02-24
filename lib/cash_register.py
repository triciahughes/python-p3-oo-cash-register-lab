#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0):
        self.discount = discount
        self.total = total
        self.items = []
        self.last_price = 0



    def add_item(self, item, price, quantity=1):
        self.quantity = quantity
        self.total += price*quantity
        self.last_price = price*quantity
        for i in range(quantity):
            self.items.append(item)
        # self.items.append(item)
        return self.items

    def void_last_transaction(self):
        self.total -= self.last_price


    def apply_discount(self, discount=0):

        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_conversion = int((self.discount / 100) * self.total)
            self.total -= discount_conversion
            # round(self.total, 0)
            print(f"After the discount, the total comes to ${self.total}.")




# register = CashRegister()
# register.add_item("cat", 1200)
# register.add_item("cat", 1200)
# register.add_item("cat", 1200)
# register.apply_discount(20)

# new_register = CashRegister()
# new_register.add_item("eggs", 1.99, 20)
# new_register.add_item("tomato", 1.76)