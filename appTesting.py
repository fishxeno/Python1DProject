import Products as _p, copy, json

# Branson
# Returns initial total and total after additional charges
def getCartTotal(cart: list[_p.Product]):  
    total = 0
    for item in cart: 
        total += item.stock * item.getPrice(isMember)
    
    # If you want to include additional charges
    totalAfterCharges = total * 1.09
    return (total,totalAfterCharges)

# Tze Jing / Branson
# Function is called when a transaction has been made, it makes the necessary stock changes 
# to the inventory variable and clears the cart 
def updateInventoryAndClearCart():
    for item in cart:
        for inventoryitem in inventory:
            if item.name == inventoryitem.name: #matches item to items in inventory 
                inventoryitem.removeStock(item.stock) #removes item from inventory
    cart.clear()     
    updateWarehouseDB() # changes are made to the mock database

# Tze Jing
# Returns a list (copy) of products from a search string - case-insensitive
# i.e - "product" -> should return all 3 items
# i.e - "product 3" -> should return product 3
def searchItem(searchString,inventory):
    result=[]
    for item in inventory:
        if searchString.lower() in item['name'].lower():
            result.append(item)
    return result

# Branson
# Update the inventory to the mock inventory database -> warehouse.json
def updateWarehouseDB():
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
            
# MAIN LOGIC FOR THE CODE STARTS HERE
# Test the business logic for the application using print/input statements before incorporating into streamlit
isMember = False
inventory = loadFromWarehouseDB()
cart = []

# Simulating adding an item to cart
itemToCart = copy.copy(inventory[0])
itemToCart.stock = 5
cart.append(itemToCart)

itemToCart = copy.copy(inventory[1])
itemToCart.stock = 10
cart.append(itemToCart)

itemToCart = copy.copy(inventory[9])
itemToCart.stock = 3
cart.append(itemToCart)

updateInventoryAndClearCart()