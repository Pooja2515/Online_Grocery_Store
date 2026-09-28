from mysql.connector import connect

connection = connect(
    host="127.0.0.1",
    user="root",
    password="Pooja1@#123",
    database="grocery_store_db",
    use_pure=True
)

cursor = connection.cursor()

print("Database Connected Successfully")