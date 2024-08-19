from pprint import pprint
import json

with open("file.json", mode="r", encoding="utf-8") as read_file:
    data = json.load(read_file)


def get_users_info(data):
    users = data.get("users", [])
    return users

def get_users_with_order(users_info):
    users_with_orders = []
    for user in users_info:
        if user["orders"]:
            users_with_orders.append(user["name"])
    print(f"Users with Orders: {users_with_orders}")    
    
def get_products_and_amounts(users_info):
    for user in users_info:
        print(f"User: {user["name"]}")
        for order in user["orders"]:
            print(f"   Product: {order["product"]}, Amount: ${order["amount"]}")
    

users_info = get_users_info(data)

# Execute the functions with the processed users data
get_users_with_order(users_info)
get_products_and_amounts(users_info)