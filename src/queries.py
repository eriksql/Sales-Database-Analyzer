import sqlite3
import pandas as pd


def get_sales_data():
    """
    Retrieves all sales data from the database.
    """

    connection = sqlite3.connect("../data/sales.db")

    query = """
    SELECT *
    FROM sales
    """

    df = pd.read_sql_query(query, connection)

    connection.close()

    return df


def get_total_revenue():
    """
    Calculates the total revenue.
    """

    connection = sqlite3.connect("../data/sales.db")

    query = """
    SELECT SUM(quantity * price) AS total_revenue
    FROM sales
    """

    result = pd.read_sql_query(query, connection)

    connection.close()

    return result


def get_customer_revenue():
    """
    Calculates the total revenue for each customer.
    """

    connection = sqlite3.connect("../data/sales.db")

    query = """
    SELECT customer,
           SUM(quantity * price) AS total_spent
    FROM sales
    GROUP BY customer
    ORDER BY total_spent DESC
    """

    result = pd.read_sql_query(query, connection)

    connection.close()

    return result


def get_total_sales():
    """
    Counts the total number of sales.
    """

    connection = sqlite3.connect("../data/sales.db")

    query = """
    SELECT COUNT(*) AS total_sales
    FROM sales
    """

    result = pd.read_sql_query(query, connection)

    connection.close()

    return result

def get_average_price():
    """
    Calculates the average product price.
    """

    connection = sqlite3.connect("../data/sales.db")

    query = """
    SELECT AVG(price) AS average_price
    FROM sales
    """

    result = pd.read_sql_query(query, connection)

    connection.close()

    return result