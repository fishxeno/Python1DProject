import streamlit as st
import mylibrary #functions
import Products

products_instance = Products.products()
# Mock data for demonstration purposes
products_instance.items = [
{"name": "Sample Product", "details": "This is a sample product.", "price": 10, "image": "./images/image1.png", "stock": 100}, 
{"name": "Another Product", "details": "This is another product.", "price": 15, "image": "./images/image2.png", "stock": 50},
{"name": "Third Product", "details": "This is the third product.", "price": 20, "image": "./images/image3.png", "stock": 30},
{"name": "Fourth Product", "details": "This is the fourth product.", "price": 25, "image": "./images/image4.png", "stock": 20},
{"name": "Fifth Product", "details": "This is the fifth product.", "price": 30, "image": "./images/image5.png", "stock": 10},
{"name": "Sixth Product", "details": "This is the sixth product.", "price": 35, "image": "./images/image6.png", "stock": 5},
{"name": "Seventh Product", "details": "This is the seventh product.", "price": 40, "image": "./images/image7.png", "stock": 2},
{"name": "Eighth Product", "details": "This is the eighth product.", "price": 45, "image": "./images/image8.png", "stock": 0},
{"name": "Ninth Product", "details": "This is the ninth product.", "price": 50, "image": "./images/image9.png", "stock": 0},
{"name": "Tenth Product", "details": "This is the tenth product.", "price": 55, "image": "./images/image10.png", "stock": 0}]

st.write("We have the following products:")

search_term = st.text_input("Search:")

for i in range(0,len(products_instance.items),2):
    col1, col2 = st.columns(2, vertical_alignment="center", gap="medium", border=True)
    # define dialog for adding to cart
    # because of the loop, need to pass i as an argument
    @st.dialog(f"Thank you for choosing {products_instance.items[i]['name']}! Please select the quantity.")
    
    def addToCart(i=i):
        
        st.write(f"You have selected {products_instance.items[i]['name']}.")
        quantity = st.number_input("Enter quantity:", min_value=1, max_value=products_instance.items[i]['stock'], value=1)
        if st.button("Add to cart"):
            st.success(f"Added {quantity} of {products_instance.items[i]['name']} to cart.")
            st.session_state.purchase = {"item": products_instance.items[i]['name'], "quantity": quantity}
            
    #columns
    with col1:
        st.text(f"- {products_instance.items[i]['name']}: {products_instance.items[i]['details']}")
        st.image(products_instance.items[i]["image"])
        if (products_instance.items[i]['stock'] != 0):
            if (st.button(f"Add to cart", key=f"button_{i}")):
                addToCart(i)
        else:
            st.button(label=f"{products_instance.items[i]['name']} is out of stock",key=f"button_{i}_out_of_stock",disabled=True)
            
    with col2:
        st.text(f"- {products_instance.items[i+1]['name']}: {products_instance.items[i+1]['details']}")
        st.image(products_instance.items[i+1]["image"])
        if (products_instance.items[i+1]['stock'] != 0):
            if (st.button(f"Add to cart", key=f"button_{i+1}")):
                addToCart(i+1)
        else:
            st.button(label=f"{products_instance.items[i+1]['name']} is out of stock",key=f"button_{i+1}_out_of_stock",disabled=True)

#checkout button and dialog
@st.dialog("Checkout")
def checkout():
    st.write("You are checking out the following item:")
    st.write(f"- {st.session_state.purchase['item']}: {st.session_state.purchase['quantity']}")
    if st.button("Confirm Purchase"):
        st.success(f"Purchase confirmed! You bought {st.session_state.purchase['quantity']} of {st.session_state.purchase['item']}.")

if st.button("Proceed to Checkout"):
    checkout()