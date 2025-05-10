from item_to_purchase import ItemToPurchase
from shopping_cart import ShoppingCart

def print_menu(cart: ShoppingCart):
    # -----------------------------
    # Step 5: print_menu() definition
    # -----------------------------
    while True:
        print(
            "\nMENU\n"
            "a - Add item to cart\n"
            "r - Remove item from cart\n"
            "c - Change item quantity\n"
            "i - Output items' descriptions\n"
            "o - Output shopping cart\n"
            "q - Quit\n"
        )
        choice = input("Choose an option:\n").strip().lower()

        if choice == 'q':
            break

        elif choice == 'a':
            # Step 8
            print("ADD ITEM TO CART")
            name  = input("Enter the item name:\n")
            desc  = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            qty   = int(input("Enter the item quantity:\n"))
            cart.add_item(ItemToPurchase(name, desc, price, qty))

        elif choice == 'r':
            # Step 9
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)

        elif choice == 'c':
            # Step 10
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            qty  = int(input("Enter the new quantity:\n"))
            cart.modify_item(ItemToPurchase(name=name, quantity=qty))

        elif choice == 'i':
            # Step 6 (descriptions)
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == 'o':
            # Step 6 (cart)
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        else:
            print("Invalid option. Please try again.")

def main():
    # -----------------------------
    # Step 7: Prompt customer & date
    # -----------------------------
    customer = input("Enter customer's name:\n")
    today    = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer}")
    print(f"Today's date: {today}")

    cart = ShoppingCart(customer, today)
    print_menu(cart)

if __name__ == "__main__":
    main()
