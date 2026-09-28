from database import connection,cursor


#Add Product
def add_product():

    name=input("Product Name: ")
    category=input("Category: ")
    price=float(input("Price: "))
    stock=int(input("Stock: "))
    cursor.execute(
        """
        INSERT INTO products
        (product_name,category,price,stock)
        VALUES(%s,%s,%s,%s)
        """,
        (name,category,price,stock)
    )
    connection.commit()
    print("Product Added Successfully.")


#View Product
def view_products():

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    print("\n===== PRODUCTS =====")
    if len(products) == 0:
        print("No Products Available.")
        return
    for product in products:
        print(f"""
Product ID : {product[0]}
Name       : {product[1]}
Category   : {product[2]}
Price      : ₹{product[3]}
Stock      : {product[4]}
-----------------------------
""")


#Search Product
def search_product():

    keyword = input("Enter Product Name: ")
    cursor.execute(
        "SELECT * FROM products WHERE product_name LIKE %s",
        ("%" + keyword + "%",)
    )
    products = cursor.fetchall()
    if len(products) == 0:
        print("No Product Found.")
        return
    print("\n===== SEARCH RESULT =====")
    for product in products:
        print(f"""
Product ID : {product[0]}
Name       : {product[1]}
Category   : {product[2]}
Price      : ₹{product[3]}
Stock      : {product[4]}
-----------------------------
""")


#Update Stock
def update_stock():

    product = int(input("Product ID: "))
    stock = int(input("New Stock: "))
    cursor.execute(
        """
        UPDATE products
        SET stock=%s
        WHERE product_id=%s
        """,
        (stock, product)
    )
    connection.commit()
    print("\nStock Updated Successfully.")


#Register Customer
def register_customer():

    print("\n===== REGISTER CUSTOMER =====")
    name = input("Customer Name: ")
    phone = input("Phone: ")
    cursor.execute(
        """
        INSERT INTO customers
        (customer_name, phone)
        VALUES(%s,%s)
        """,
        (name, phone)
    )
    connection.commit()
    print("\nCustomer Registered Successfully.")


#Place Order
def place_order():

    customer = int(input("Customer ID: "))
    product = int(input("Product ID: "))
    quantity = int(input("Quantity: "))
    cursor.execute(
        "SELECT price, stock FROM products WHERE product_id=%s",
        (product,)
    )
    data = cursor.fetchone()
    if data is None:
        print("Product Not Found.")
        return
    price = data[0]
    stock = data[1]
    if quantity > stock:
        print("Not Enough Stock.")
        return
    total = price * quantity
    cursor.execute(
        """
        INSERT INTO orders
        (customer_id, product_id, quantity, total_price)
        VALUES(%s,%s,%s,%s)
        """,
        (customer, product, quantity, total)
    )
    cursor.execute(
        "UPDATE products SET stock=stock-%s WHERE product_id=%s",
        (quantity, product)
    )
    connection.commit()
    print("\nOrder Placed Successfully.")


#Generate Bill
def generate_bill():

    customer = int(input("Customer ID: "))
    cursor.execute(
        "SELECT * FROM orders WHERE customer_id=%s",
        (customer,)
    )
    orders = cursor.fetchall()
    total = 0
    print("\n========== BILL ==========")
    for order in orders:
        print(order)
        total += order[4]
    print("----------------------")
    print("Total Bill: ₹", total)


#View Order History
def order_history():

    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    print("\n===== ORDER HISTORY =====")
    if len(orders) == 0:
        print("No Orders Found.")
        return
    for order in orders:
        print(order)