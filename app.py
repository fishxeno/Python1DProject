import streamlit as st
import mylibrary #functions
import Products as _p
import appTesting

IMAGE_PATH = "./images/"
# Integration of inventory system - inventory is never changed
inventory = appTesting.loadFromWarehouseDB()
cart = []

# Inject CSS (Styling) code 
st.html("""
        <style>
        [data-testid="stColumn"] {
            background-color: rgba(112, 128, 144, 0.15);
            padding: 1rem;
            border-radius: 8px;
        }

        [data-testid="stColumn"]:has([data-testid="stVerticalBlock"]:empty) {
            visibility: hidden;
        }
        </style>
        """)


st.write("We have the following products:")

# We will display the filtered items here
search_term = st.text_input("Search:") 
filteredProducts = appTesting.searchItem(search_term,inventory)

# Information logic for filtered products
if len(filteredProducts) == 0:
    st.warning("No results found, please try again")
elif len(filteredProducts) != len(inventory):
    st.info("There are {} results for {} ".format(len(filteredProducts),search_term))

for i in range(0,len(filteredProducts),2):

    col1, col2 = st.columns(2, vertical_alignment="center", gap="medium", border=False)
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
    
    if len(filteredProducts) > 1:
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