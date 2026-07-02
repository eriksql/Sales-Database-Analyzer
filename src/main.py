from database import create_database
from queries import (
    get_sales_data,
    get_total_revenue,
    get_customer_revenue,
    get_total_sales,
    get_average_price
)

# Create database
create_database()

# Retrieve all sales
sales = get_sales_data()

print("Sales Data\n")
print(sales)

# Display total revenue
print("\nTotal Revenue\n")

total = get_total_revenue()

print(total)

# Display revenue by customer
print("\nRevenue by Customer\n")

customer_revenue = get_customer_revenue()

print(customer_revenue)

# Display total number of sales
print("\nTotal Sales\n")

total_sales = get_total_sales()

print(total_sales)

print("\nAverage Product Price\n")

average_price = get_average_price()

print(average_price)