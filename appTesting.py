import Products as _p, copy

# Returns initial total and total after additional charges
def getCartTotal(cart: list[_p.Product]):  
    total = 0
    for item in cart: 
        total += item.stock * item.getPrice(isMember)
    
    # If you want to include additional charges
    totalAfterCharges = total * 1.09
    return (total,totalAfterCharges)

# Function is called when a transaction has been made, it makes the necessary stock changes 
# to the inventory variable and clears the cart 
def updateInventoryAndClearCart():
    for item in cart:
        for inventoryitem in inventory:
            if item.name == inventoryitem.name: #matches item to items in inventory 
                inventoryitem.removeStock(item.stock) #removes item from inventory
    cart.clear()     


# Returns a list (copy) of products from a search string - case-insensitive
# i.e - "product" -> should return all 3 items
# i.e - "product 3" -> should return product 3
def searchItem(searchString):
    result=[]
    for item in inventory:
        if searchString.lower() in item.name.lower():
            result.append(item)
    return result

# MAIN LOGIC FOR THE CODE STARTS HERE
# Test the business logic for the application using print/input statements before incorporating into streamlit
isMember = False
inventory = [
    _p.Product(name="Product 1", price=15, stock=15),
    _p.Product(name="Product 2", price=35.50, stock=15),
    _p.Product(name="Product 3", price=22, stock=90)
]
cart = []

# Simulating adding an item to cart
itemToCart = copy.copy(inventory[0])
itemToCart.stock = 5
cart.append(itemToCart)

itemToCart = copy.copy(inventory[1])
itemToCart.stock = 10
cart.append(itemToCart)

itemToCart = copy.copy(inventory[2])
itemToCart.stock = 3
cart.append(itemToCart)

# print total
print("Total", getCartTotal(cart))

