# -----------------------------
# Step 1: Define ItemToPurchase
# -----------------------------
class ItemToPurchase:
    def __init__(self, name="none", price=0.0, quantity=0):
        self.item_name     = name
        self.item_price    = price
        self.item_quantity = quantity

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total:.0f}")

# -----------------------------
# Steps 2 & 3: Prompt & Total
# -----------------------------
def main():
    # Step 2: Prompt for two items
    print("Item 1")
    name1  = input("Enter the item name:\n")
    price1 = float(input("Enter the item price:\n"))
    qty1   = int(input("Enter the item quantity:\n"))

    print("\nItem 2")
    name2  = input("Enter the item name:\n")
    price2 = float(input("Enter the item price:\n"))
    qty2   = int(input("Enter the item quantity:\n"))

    # Create objects
    item1 = ItemToPurchase(name1, price1, qty1)
    item2 = ItemToPurchase(name2, price2, qty2)

    # Step 3: Print individual costs + total
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total_cost = price1 * qty1 + price2 * qty2
    print(f"Total: ${total_cost:.0f}")

if __name__ == "__main__":
    main()
