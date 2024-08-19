from pprint import pprint
import json

with open("file.json", mode="r", encoding="utf-8") as read_file:
    data = json.load(read_file)


def get_users_info(data):
    if "users" in data:
        return data["users"]
    []


def get_orders_info(users_info):
    orders_info_dict = {}
    for user in users_info:
        orders_info_dict[user["name"]] = user["orders"] 
    return orders_info_dict           
            
def get_orders_amount(orders_info):
    orders_amount_dict = {}
    for order in orders_info:
        orders_amount_dict[order["product"]] = order["amount"] 
    return orders_amount_dict

def get_users_with_orders(users_info):
    users_with_orders = []
    for user in users_info:
        if user["orders"]:  # Check if the user has orders
            users_with_orders.append(user)
        return users_with_orders

     
    
        





users_info = get_users_info(data) 
print("Users Info:", users_info)

orders_info = get_orders_info(users_info)
print("Order Info:", orders_info)

orders_amount = get_orders_amount(orders_info)
print("Order Amount:", orders_amount)

info_of_users_with_orders = get_users_with_orders(users_info)
print("Users with Orders:", info_of_users_with_orders)