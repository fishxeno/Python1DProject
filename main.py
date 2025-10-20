import streamlit as st
import appfunctions
import copy
from PIL import Image

# Initialize Variables
_SS = st.session_state

st.title(":blue[Kiki's Pet Food Delivery Service!]")
st.subheader(":red[DISCOUNTS:]")
st.markdown(":blue[**- 2 products** :dog: **for 10% off**]")
st.markdown(":blue[**- 3 products** :cat: **for 20% off**]")
st.markdown(":blue[**- 4 products** :rabbit: **for 30% off**]")
st.markdown(":blue[**- 5 products** :fish: **for 40% off**]")
st.markdown(":blue[**- 6 products** :hamster: **for 50% off**]")
st.image("images/image11.png")
st.subheader("**:red[What are you waiting for,shop our products below]:cat: :red[!!!]**")

# We will display the filtered items here
search_term = st.text_input("Search:") 
_SS["dispProds"] = appfunctions.searchItem(search_term,_SS["inventory"])

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

# show toast if purchase successful
if _SS.show_added_to_cart:
    _SS.show_added_to_cart = False
    st.toast(_SS.addToCart_message, duration=3)

if st.button("Clear Cart", disabled=(len(_SS["cart"])==0)):
    # 20/10/2025 - Fixed cart clear issue
    _SS["cart"].clear() 
    _SS["inventory"] = copy.deepcopy(_SS["inventory_copy"])
    _SS["dispProds"] = appfunctions.searchItem(search_term,_SS["inventory"])
    st.rerun()
    st.toast("Cart cleared!", duration=3)

# define dialog for adding to cart
# because of the loop, need to pass i as an argument
@st.dialog(f"Thank you for choosing this product! Please select the quantity:")
def addToCart(i=int):
    #enable checkout button
    _SS.checkout_btn_disabled = False

    product = _SS["dispProds"][i]
    st.write(f"You have selected {product.name}")
    st.text(f"Stock: {product.stock}")
    quantity = st.number_input("Enter quantity:", min_value=1, max_value=product.stock, value=1)

    if st.button("Add to cart"):
        # Remove from inventory and filtered products (frontend)
        _SS["dispProds"][i].updateStock(-quantity)
        _SS.show_added_to_cart = True
        _SS.addToCart_message = f"Added {quantity} of {product.name} to cart."
        # Add to cart in session state
        for cartItem in _SS["cart"]:
            if cartItem["item"] == product.name:
                cartItem["quantity"] += quantity
                break
        else:
            _SS["cart"].append({"item": product.name, "quantity": quantity, "price": product.price})
        st.rerun()

# UI
st.write("We have the following products:")

# Information logic for filtered products
if len(_SS["dispProds"]) == 0:
    st.warning("No results found, please try again")
elif len(_SS["dispProds"]) != len(_SS["inventory"]):
    st.info("There are {} results for '{}'. ".format(len(_SS["dispProds"]),search_term))

# Branson - wrote product card as function
def drawProductCard(index, col):
    product = _SS["dispProds"][index]
    with col:
        st.image(product.image, width="stretch")
        st.markdown(f"##### {product.name}")
        st.markdown(f"#### ${product.price}")
        if 0 < product.stock < 5: 
            st.badge("Few items remaining")
        elif product.stock == 0: 
            st.badge("Out of stock", color="red")
        st.button(f"🛒 Add to cart", key=f"button_{index}", on_click=addToCart, args=(index,),
                    disabled=product.stock == 0)
        expander = st.expander("Product Description")
        expander.write(product.details)
    
for i in range(0,len(_SS["dispProds"]),2):
    (col1, col2) = st.columns(2, vertical_alignment="center", gap="medium", border=False)
    #columns
    drawProductCard(i , col1)
    if i+1 != len(_SS["dispProds"]):
        drawProductCard(i+1 , col2)
    