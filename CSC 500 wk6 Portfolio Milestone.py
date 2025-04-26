class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
    
    def remove_item(self, item_name):
        found = False
        for i, item in enumerate(self.cart_items):
            if item.name == item_name:
                self.cart_items.pop(i)
                found = True
                break
        
        if not found:
            print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item_to_purchase):
        found = False
        for i, item in enumerate(self.cart_items):
            if item.name == item_to_purchase.name:
                found = True
                if item_to_purchase.description != "none":
                    self.cart_items[i].description = item_to_purchase.description
                if item_to_purchase.price != 0:
                    self.cart_items[i].price = item_to_purchase.price
                if item_to_purchase.quantity != 0:
                    self.cart_items[i].quantity = item_to_purchase.quantity
                break
        
        if not found:
            print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.quantity
        return num_items
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.price * item.quantity)
        return total_cost
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(f"{item.name} {item.quantity} @ ${item.price} = ${item.quantity * item.price}")
            print(f"Total: ${self.get_cost_of_cart()}")
    
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")


def print_menu(cart):
    menu = '''MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit'''
    
    choice = ''
    while choice != 'q':
        print(menu)
        choice = input("Choose an option: ")
        
        if choice == 'a':
            print("ADD ITEM TO CART")
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = int(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            
            item = ItemToPurchase(name, description, price, quantity)
            cart.add_item(item)
            
        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)
            
        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name: ")
            quantity = int(input("Enter the new quantity: "))
            
            item = ItemToPurchase(name, quantity=quantity)
            cart.modify_item(item)
            
        elif choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
            
        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()
            
        elif choice == 'q':
            pass
        else:
            print("Invalid option. Please try again.")
        
        print()  # Print blank line for better readability


def main():
    print("Enter customer's name:")
    customer_name = input()
    
    print("Enter today's date:")
    current_date = input()
    
    print("\nCustomer name: " + customer_name)
    print("Today's date: " + current_date)
    print()
    
    cart = ShoppingCart(customer_name, current_date)
    
    print_menu(cart)


if __name__ == "__main__":
    main()