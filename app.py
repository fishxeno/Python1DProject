import streamlit as st
import mylibrary #functions
import Products as _p
import appTesting

IMAGE_PATH = "./images/"
# Integration of inventory system - inventory is never changed
inventory = [
    _p.Product(name="Product 1", price=10, stock=100, image=f"{IMAGE_PATH}/image1.png"),
    _p.Product(name="Product 2", price=15, stock=50, image=f"{IMAGE_PATH}/image2.png"),
    _p.Product(name="Product 3", price=20, stock=30, image=f"{IMAGE_PATH}/image3.png"),
    _p.Product(name="Product 4", price=25, stock=20, image=f"{IMAGE_PATH}/image4.png"),
    _p.Product(name="Product 5", price=30, stock=10, image=f"{IMAGE_PATH}/image5.png"),
    _p.Product(name="Product 6", price=35, stock=5, image=f"{IMAGE_PATH}/image6.png"),
    _p.Product(name="Product 7", price=40, stock=2, image=f"{IMAGE_PATH}/image7.png"),
    _p.Product(name="Product 8", price=45, image=f"{IMAGE_PATH}/image8.png"),
    _p.Product(name="Product 9", price=50, image=f"{IMAGE_PATH}/image9.png"),
    _p.Product(name="Product 10", price=55, image=f"{IMAGE_PATH}/image10.png")
]

# We will display the filtered items here
filteredProducts = inventory[:]
cart = []

st.write("We have the following products:")

search_term = st.text_input("Search:") #search bar 
search_results = appTesting.searchItem(search_term,inventory)
if search_term:
    if search_results:
        st.write("There are {} results for {} ".format(len(search_results),search_term))
        col1, col2 = st.columns(2, vertical_alignment="center", gap="medium", border=True)
        for i in range(0, len(search_results), 2):
            with col1:
                st.write("Product:{}".format(search_results[i]['name']))
                st.image(search_results[i]['image'])
                st.write("Price:{}".format(search_results[i]['price']))
                st.write("Stock:{}".format(search_results[i]['stock']))
            with col2:
                if i + 1 < len(search_results):
                    st.write("Product:{}".format(search_results[i+1]['name']))
                    st.image(search_results[i+1]['image'])
                    st.write("Price:{}".format(search_results[i+1]['price']))
                    st.write("Stock:{}".format(search_results[i+1]['stock']))                   
    else:  
        st.warning("No results found, please try again")
else:
    st.info("Search:")



for i in range(0,len(filteredProducts),2):
    col1, col2 = st.columns(2, vertical_alignment="center", gap="medium", border=True)
    # define dialog for adding to cart
    # because of the loop, need to pass i as an argument
    @st.dialog(f"Thank you for choosing {filteredProducts[i].name}! Please select the quantity.")
    
    def addToCart(i=i):
        
        st.write(f"You have selected {filteredProducts[i].name}.")
        quantity = st.number_input("Enter quantity:", min_value=1, max_value=filteredProducts[i].stock, value=1)
        if st.button("Add to cart"):
            st.success(f"Added {quantity} of {filteredProducts[i].name} to cart.")
            st.session_state.purchase = {"item": filteredProducts[i].name, "quantity": quantity}
            
    #columns
    with col1:
        st.text(f"- {filteredProducts[i].name}: {filteredProducts[i].details}")
        st.image(filteredProducts[i].image)
        if (filteredProducts[i].stock != 0):
            if (st.button(f"Add to cart", key=f"button_{i}")):
                addToCart(i)
        else:
            st.button(label=f"{filteredProducts[i].name} is out of stock",key=f"button_{i}_out_of_stock",disabled=True)
            
    with col2:
        st.text(f"- {filteredProducts[i+1].name}: {filteredProducts[i+1].details}")
        st.image(filteredProducts[i+1].image)
        if (filteredProducts[i+1].stock != 0):
            if (st.button(f"Add to cart", key=f"button_{i+1}")):
                addToCart(i+1)
        else:
            st.button(label=f"{filteredProducts[i+1].name} is out of stock",key=f"button_{i+1}_out_of_stock",disabled=True)

#checkout button and dialog
@st.dialog("Checkout")
def checkout():
    st.write("You are checking out the following item:")
    st.write(f"- {st.session_state.purchase['item']}: {st.session_state.purchase['quantity']}")
    if st.button("Confirm Purchase"):
        st.success(f"Purchase confirmed! You bought {st.session_state.purchase['quantity']} of {st.session_state.purchase['item']}.")

if st.button("Proceed to Checkout"):
    checkout()