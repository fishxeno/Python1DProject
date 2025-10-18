import streamlit as st
import appTesting

# Initialize session state
_SS = st.session_state

if "inventory" not in _SS: _SS["inventory"] = appTesting.loadFromWarehouseDB()
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
            background-color: red;
            background-size: cover;
            background-image: url("https://images.wallpapersden.com/image/download/mountains-silhouette_a21ubWqUmZqaraWkpJRoZWWtaGVl.jpg");
            margin-bottom: 20px
        }
        div[data-testid="stSidebarNav"]{
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


pg = st.navigation([st.Page("main.py", title="Our Products", default=True), 
                    st.Page("checkout.py", title="My Cart")])
pg.run()

