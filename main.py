from functions import add_product,view_products,search_product,update_stock,register_customer,place_order,generate_bill,order_history

while True:

    print("\n========== ONLINE GROCERY STORE ==========")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Register Customer")
    print("6. Place Order")
    print("7. Generate Bill")
    print("8. View Order History")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_stock()

    elif choice == "5":
        register_customer()

    elif choice == "6":
        place_order()

    elif choice == "7":
        generate_bill()

    elif choice == "8":
        order_history()

    elif choice == "9":
        print("Thank You for using Online Grocery Store.")
        break

    else:
        print("Invalid Choice.")