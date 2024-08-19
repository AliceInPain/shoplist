from pprint import pprint
import json

with open("file.json", mode="r", encoding="utf-8") as read_file:
    data = json.load(read_file)


 




# name of the users who ordered
users_with_order = []  # storing the names of users who purchased a product
for user in data["users"]:  # []--> to access a key in a dictionary
    if user["orders"]:
        users_with_order.append(user["name"])
pprint(users_with_order)  # displays --> ['John Doe', 'Jane Smith']
    
    
           

# list of products + amount
for user in data["users"]:
    user_name = user["name"]
    print(user_name)
    for order in user["orders"]:
        list_of_products = (order["product"], order["amount"])
        pprint(list_of_products)
        # displays -->
        # John Doe
        # ('Laptop', 1200.5)
        # ('Smartphone', 800.75)
        # Jane Smith
        # ('Tablet', 300.0)
        
        
# # list of products + name and amount
orders_info = {}
for user in data["users"]:
    if user["name"] not in orders_info:
        orders_info[user["name"]] = []

    for order in user["orders"]:
        user_details = {"Product": order["product"], "Amount": order["amount"]}
        orders_info[user["name"]].append(user_details)

for user, item in orders_info.items():
    print(f"User:{user}")
    for order in item:
        print(f"    Product: {order["Product"]},\n    Amount: ${order["Amount"]}")
        #displays:
        # User:John Doe
        #     Product: Laptop,
        #     Amount: $1200.5
        #     Product: Smartphone,
        #     Amount: $800.75
        # User:Jane Smith
        #     Product: Tablet,
        #     Amount: $300.0