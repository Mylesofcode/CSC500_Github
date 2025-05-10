# -----------------------------
# Step 4b: ShoppingCart class
# -----------------------------
from item_to_purchase import ItemToPurchase

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date  = current_date
        self.cart_items    = []

    def add_item(self, item: ItemToPurchase):
        # Step 8: Adds an item to cart
        self.cart_items.append(item)

    def remove_item(self, item_name: str):
        # Step 9: Removes by name
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item: ItemToPurchase):
        # Step 10: Change qty/price/description
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0.0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self) -> int:
        return sum(i.item_quantity for i in self.cart_items)

    def get_cost_of_cart(self) -> float:
        return sum(i.item_price * i.item_quantity for i in self.cart_items)

    def print_total(self):
        # Step 6 (Output shopping cart)
        print(f"{self.customer_name}'s Shopping Cart – {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        for item in self.cart_items:
            item.print_item_cost()
        print(f"Total: ${self.get_cost_of_cart():.0f}")

    def print_descriptions(self):
        # Step 6 (Output item descriptions)
        print(f"{self.customer_name}'s Shopping Cart – {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()
