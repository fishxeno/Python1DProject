import streamlit as st
import appTesting
from PIL import Image

# Initialize Variables
_SS = st.session_state
if "inventory" not in _SS: _SS["inventory"] = appTesting.loadFromWarehouseDB()
if "cart" not in _SS: _SS["cart"] = []
if "dispProds" not in _SS: _SS["dispProds"] = [] # dispProds - Displayed products

if "checkout_btn_disabled" not in st.session_state:
    st.session_state.checkout_btn_disabled = False
if "show_checkout_success" not in st.session_state:
    st.session_state.show_checkout_success = False

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
_SS["dispProds"] = appTesting.searchItem(search_term,_SS["inventory"][:]) # This is to prevent overwriting the current stock from initial stock from inventory

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

#checkout button and dialog
@st.dialog("Checkout", on_dismiss='rerun')
def checkout():
    st.write("You are checking out the following item:")
    total, discounted_amount, tax, overalltotal = appTesting.getCartTotal(_SS["cart"])
    # TODO -- IMPLEMENT LOGIC TO ALLOW USER TO MAKE QUANTITY CHANGES IN THE CHECKOUT MODAL
    for cartItem in _SS['cart']:
        st.write(f"- {cartItem['item']}: x{cartItem['quantity']}")
        st.write("SubTotal: ${:.2f}".format(cartItem['quantity'] * cartItem['price']))
    st.write("Discount: ${:.2f}".format(discounted_amount))
    st.write("GST Tax: ${:.2f}".format(tax))
    st.write("Total: ${:.2f}".format(overalltotal))
    if st.button("Confirm Purchase", disabled=st.session_state.checkout_btn_disabled):
        #disable the button after clicking, show success toast message
        st.session_state.checkout_btn_disabled = True
        st.session_state.show_checkout_success = True
        st.success(f"Purchase confirmed!")
        appTesting.updateWarehouseDB(_SS["inventory"])
        st.rerun()

# show toast if purchase successful
if st.session_state.show_checkout_success:
    st.toast("Purchase successful!", duration=6000)
    st.session_state.show_checkout_success = False

if st.button("Clear Cart", disabled=(len(_SS["cart"])==0)):
    _SS["cart"].clear() #clear cart
    _SS["dispProds"] = appTesting.searchItem(search_term,_SS["inventory"][:]) #reset displayed products to initial stock TODO bugged
    st.rerun()
    st.toast("Cart cleared!", duration=3000)

# define dialog for adding to cart
# because of the loop, need to pass i as an argument
@st.dialog(f"Thank you for choosing this product! Please select the quantity:")
def addToCart(i=int):
    #enable checkout button
    st.session_state.checkout_btn_disabled = False
    
    product = _SS["dispProds"][i]
    st.write(f"You have selected {product.name}")
    st.text(f"Stock: {product.stock}")
    quantity = st.number_input("Enter quantity:", min_value=1, max_value=product.stock, value=1)

    if st.button("Add to cart"):
        st.success(f"Added {quantity} of {product.name} to cart.")

        # Remove from inventory and filtered products (frontend)
        _SS["dispProds"][i].removeStock(quantity)

        # Add to cart in session state
        for cartItem in _SS["cart"]:
            if cartItem["item"] == product.name:
                cartItem["quantity"] += quantity
                break
        else:
            _SS["cart"].append({"item": product.name, "quantity": quantity, "price": product.price})
        st.rerun()

# UI
if st.button("Proceed to Checkout", disabled=(len(_SS["cart"])==0)):
    checkout()

st.write("We have the following products:")

# Information logic for filtered products
if len(_SS["dispProds"]) == 0:
    st.warning("No results found, please try again")
elif len(_SS["dispProds"]) != len(_SS["inventory"]):
    st.info("There are {} results for {} ".format(len(_SS["dispProds"]),search_term))


for i in range(0,len(_SS["dispProds"]),2):
    (col1, col2) = st.columns(2, vertical_alignment="center", gap="medium", border=False)
    
    #columns
    with col1:
        st.text(f"- {_SS["dispProds"][i].name}: {_SS["dispProds"][i].details}")
        st.image(_SS["dispProds"][i].image)
        if (_SS["dispProds"][i].stock != 0):
            if (st.button(f"Add to cart", key=f"button_{i}")):
                addToCart(i)
        else:
            st.button(label=f"{_SS["dispProds"][i].name} is out of stock",key=f"button_{i}_out_of_stock",disabled=True)
    
    if i+1 != len(_SS["dispProds"]):
        with col2:
            st.text(f"- {_SS["dispProds"][i+1].name}: {_SS["dispProds"][i+1].details}")
            st.image(_SS["dispProds"][i+1].image)
            if (_SS["dispProds"][i+1].stock != 0):
                if (st.button(f"Add to cart", key=f"button_{i+1}")):
                    addToCart(i+1)
            else:
                st.button(label=f"{_SS["dispProds"][i+1].name} is out of stock",key=f"button_{i+1}_out_of_stock",disabled=True)