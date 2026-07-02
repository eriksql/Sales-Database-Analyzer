import sqlite3


def create_database():
    """
    Creates the sales database and inserts sample data.
    """

    connection = sqlite3.connect("../data/sales.db")
    cursor = connection.cursor()

    # Remove existing table
    cursor.execute("""
    DROP TABLE IF EXISTS sales
    """)

    # Create table
    cursor.execute("""
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer TEXT,
        product TEXT,
        category TEXT,
        quantity INTEGER,
        price REAL
    )
    """)

    # Sample data
    sales_data = [
        ("John", "Laptop", "Electronics", 1, 1200.00),
        ("Mary", "Keyboard", "Electronics", 2, 80.00),
        ("Alice", "Desk", "Furniture", 1, 350.00),
        ("John", "Mouse", "Electronics", 3, 25.00),
        ("Bob", "Chair", "Furniture", 2, 150.00),
        ("Alice", "Monitor", "Electronics", 2, 280.00)
    ]

    cursor.executemany("""
    INSERT INTO sales
    (customer, product, category, quantity, price)
    VALUES (?, ?, ?, ?, ?)
    """, sales_data)

    connection.commit()
    connection.close()

    print("Database created successfully.")