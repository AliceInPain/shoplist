from pprint import pprint
import json

with open("file.json", mode="r", encoding="utf-8") as read_file:
    data = json.load(read_file)



# USERS is a list of dictionaries

for key, value in data.items():
    if key == "users":
        for user in value:
            user_order = user["orders"]
            user_name = user["name"]
            if user_order:
                print(user_name)  # displays --> John Do Jane Smith


for key, value in data.items():
    if key == "users":
        for user in value:
            user_order = user["orders"]
            user_name = user["name"]
            for order in user_order:
                user_amount = order["amount"]
                user_product = order["product"]
                print(f"Product: {user_product}, Amount: {user_amount}")


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
