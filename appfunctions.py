import Products as _p, json

# Branson / Tze Jing
# Returns initial total and total after additional charges
def getCartTotal(cart: list[_p.Product]):  
    total = 0
    quantity = 0
    for item in cart: 
        total = total + item["quantity"] * item["price"]
        quantity = quantity + item["quantity"]
    # My absolutely cooked code for discounts - Tze Jing
    discount_rates = {2:0.1, 3:0.2, 4:0.3, 5:0.4}
    if quantity >= 6:
        discount = 0.5
    else:
        discount = discount_rates.get(quantity,0)
    discounted_amount = (total*discount)
    after_discount = (total*(1-discount))
    tax = after_discount*0.09
    overalltotal = after_discount*1.09
    return (total,discounted_amount,tax,overalltotal)

# Tze Jing
# Returns a list (copy) of products from a search string - case-insensitive
# i.e - "product" -> should return all 3 items
# i.e - "product 3" -> should return product 3
def searchItem(searchString,inventory: list[_p.Product]):
    result=[]
    for item in inventory:
        if searchString.lower() in item.name.lower():
            result.append(item)
    return result

# Branson
# Update the inventory to the mock inventory database -> warehouse.json
def updateWarehouseDB(inventory):
    # Convert the inventory database to a list of dictionaries, for conversion to JSON
    inventory_as_dict = []
    for item in inventory:
        inventory_as_dict.append(item.__dict__)

    # Overwrite the list into warehouse file
    with open("warehouse.json", "w") as f:
        json.dump(inventory_as_dict, f, indent=4)

# Branson
# Retrieve the inventory from the database file -> warehouse.json 
# It then creates new Product instances (with loaded values) to be added to an inventory list 
# Returns the loaded inventory list
def loadFromWarehouseDB():
    with open("warehouse.json", "r") as f:
        loaded_items = json.load(f)
        inventory = [] # not the same as the one outside the function

        for item in loaded_items:
            inventory.append(_p.Product(name=item["name"], details=item["details"], price=item["price"],
                                        stock=item["stock"], image=item["image"] ))
            
        return inventory
            