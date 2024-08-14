from pprint import pprint

data = {
    "users": [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john@example.com",
            "address": {
                "street": "123 Elm St",
                "city": "Springfield",
                "zipcode": "12345"
            },
            "orders": [
                {
                    "order_id": 101,
                    "product": "Laptop",
                    "amount": 1200.50
                },
                {
                    "order_id": 102,
                    "product": "Smartphone",
                    "amount": 800.75
                }
            ]
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "email": "jane@example.com",
            "address": {
                "street": "456 Oak St",
                "city": "Greendale",
                "zipcode": "67890"
            },
            "orders": [
                {
                    "order_id": 103,
                    "product": "Tablet",
                    "amount": 300.00
                }
            ]
        }
    ]
}

# USERS is a list of dictionaries


# name of the users who ordered
# users_with_order = []  # storing the names of users who purchased a product
# for user in data["users"]:  # []--> to access a key in a dictionary
#     if user["orders"]:
#         users_with_order.append(user["name"])
# pprint(users_with_order)  # displays --> ['John Doe', 'Jane Smith']

for key, value in data.items():
    if key == "users":
        for user in value:
            user_order = user["orders"]
            user_name = user["name"]
            if user_order:
                print(user_name)  # displays --> John Do Jane Smith

# list of products + amount
# list_of_products = []
# for user in data["users"]:
#     for order in user["orders"]:
#         list_of_products.append((order["product"], order["amount"]))
# # displays --> [('Laptop', 1200.5), ('Smartphone', 800.75), ('Tablet', 300.0)]
# pprint(list_of_products)

for key, value in data.items():
    if key == "users":
        for user in value:
            user_order = user["orders"]
            user_name = user["name"]
            for order in user_order:
                user_amount = order["amount"]
                user_product = order["product"]
                print(f"Product: {user_product}, Amount: {user_amount}")

# # list of products + name and amount
# orders_info = {}
# for user in data["users"]:
#     # print(user["name"])
#     if user["name"] not in orders_info:
#         orders_info[user["name"]] = []

#     for order in user["orders"]:
#         user_details = {"Product": order["product"], "Amount": order["amount"]}
#         orders_info[user["name"]].append(user_details)
# # print(orders_info) #--> [{'User': 'John Doe', 'Product': 'Laptop', 'Amount': 1200.5}, {'User': 'John Doe', 'Product': 'Smartphone', 'Amount': 800.75}, {'User': 'Jane Smith', 'Product': 'Tablet', 'Amount': 300.0}]


# for user, item in orders_info.items():
#     print(f"User:{user}")
#     for order in item:
#         print(f"    Product: {order["Product"]},\n    Amount: ${order["Amount"]}")

for key, value in data.items():
    if key == "users":
        for user in value:
            user_name = user["name"]
            user_order = user["orders"]
            print(f"User: {user_name}")
            for order in user_order:
                product_name = order["product"]
                product_amount = order["amount"]
                print(f"   Product: {product_name}, Amount: ${product_amount}")
