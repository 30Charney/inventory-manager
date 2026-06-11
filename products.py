import sqlite3

def add_product(name, quantity, price):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)",
        (name, quantity, price)
    )

    conn.commit()
    conn.close()

def list_products():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    for product in cursor.fetchall():
        print(product)

    conn.close()
