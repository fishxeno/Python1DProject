import streamlit as st
import appfunctions
import copy

# Initialize session state
_SS = st.session_state

if "inventory" not in _SS: _SS["inventory"] = appfunctions.loadFromWarehouseDB()
if "inventory_copy" not in _SS: _SS["inventory_copy"] = copy.deepcopy(_SS["inventory"]) # Keep a copy of the loaded items
if "cart" not in _SS: _SS["cart"] = []
if "dispProds" not in _SS: _SS["dispProds"] = [] # dispProds - Displayed products


# Initialize Button state variables
if "checkout_btn_disabled" not in  _SS:
    _SS.checkout_btn_disabled = False
if "show_checkout_success" not in  _SS:
    _SS.show_checkout_success = False
if "show_added_to_cart" not in _SS:
    _SS.show_added_to_cart = False
    _SS.addToCart_message = ""

st.markdown(
"""
    <style>
    :root {
    --logo-height: 330px;
    }
    div[data-testid="stSidebarNav"]:before {
    content: "";
    display: block; 
    height: 300px;
    width: 300px;
    background-color: transparent;
    background-size: cover;
    background-image: url("https://i.imgur.com/ERnMZPl.png");
    margin: 1px;
    margin-top: -45px;
    }
    div[data-testid="stSidebarNav"]{
    }
    s</style>
""",
unsafe_allow_html=True,
)

pg = st.navigation([st.Page("main.py", title="Our Products", default=True), 
                    st.Page("checkout.py", title=f"🛒 My Cart - {len(_SS['cart'])} items")])
pg.run()

with st.sidebar:
    if st.button("Clear Cart", disabled=(len(_SS["cart"])==0)):
    # 20/10/2025 - Fixed cart clear issue
        _SS["cart"].clear() 
        _SS["inventory"] = copy.deepcopy(_SS["inventory_copy"])
        st.rerun()
        st.toast("Cart cleared!", duration=3)