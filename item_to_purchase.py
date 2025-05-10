# -----------------------------
# Step 4a: ItemToPurchase class
# -----------------------------
class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0.0, quantity=0):
        self.item_name        = name
        self.item_description = description
        self.item_price       = price
        self.item_quantity    = quantity

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total:.0f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")
