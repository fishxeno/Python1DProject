import streamlit as st
import appfunctions
import copy
# Initialize Variables
st.title("My Cart 🛒")
_SS = st.session_state

@st.dialog(f"✏️ Edit Product Quantity")
def editProduct(item, index):
    product = None
    product_index = 0
    initial_quantity = item['quantity']
    for prod in _SS["dispProds"]:
        if prod.name == item['item']:
           product = prod
           product_index = _SS["dispProds"].index(prod)

    st.write(f"You have selected {item['item']}")
    st.write(f"Remaining stock: {product.stock}")
    new_quantity = st.number_input("Enter quantity:", min_value=1, max_value=item['quantity']+product.stock, value=item['quantity'])
    if st.button("OK"):
        print(_SS["cart"][index])
        # Check for changes in quantity
        diff = new_quantity - initial_quantity
        _SS["dispProds"][product_index].updateStock(-diff)
        _SS["cart"][index]["quantity"] += diff
        st.rerun()

@st.dialog(f"❌ Remove Product")
def removeProduct(item):
    st.write(f"Remove the product - {item['item']} from your cart?")
    if st.button("OK"):
        for prod in _SS["dispProds"]:
            if prod.name == item['item']:
                prod.updateStock(item['quantity'])
        _SS["cart"].remove(item)
        st.rerun()

@st.dialog("Checkout", on_dismiss='rerun')
def checkout():
    st.write("Confirm your purchase?")
    if st.button("Confirm Purchase", disabled=_SS.checkout_btn_disabled):
        #disable the button after clicking, show success toast message
        _SS.checkout_btn_disabled = True
        _SS.show_checkout_success = True
        appfunctions.updateWarehouseDB(_SS["inventory"])
        _SS["inventory_copy"] = copy.deepcopy(_SS["inventory"]) # update inventory copy
        _SS["cart"].clear() #clear cart
        st.rerun()

# Show a toast if the purchase has been made
if _SS.show_checkout_success:
    st.toast("Purchase successful!", duration=6)
    _SS.show_checkout_success = False

#UI
if len(_SS["cart"]) == 0:
    st.write("Your cart is currently empty. Feel free to browse our products.")
else:
    st.write("You have purchased the following items")
    # Declare columns
    (h_col1, h_col2, h_col3, h_col4, h_col5) = st.columns([0.50, 0.1, 0.2, 0.1, 0.1], vertical_alignment="center", gap=None, border=False)

    # Declare columns 2
    h_col1.markdown("**Product**")
    h_col2.markdown("**Qty**")
    h_col3.markdown("**Subtotal($)**")
    h_col4.markdown("--")
    h_col5.markdown("--")
    
    st.markdown("<hr/>", unsafe_allow_html=True)
    (col1, col2, col3, col4, col5) = st.columns([0.50, 0.1, 0.2, 0.1, 0.1], vertical_alignment="center", gap=None, border=False)
    
    for item in _SS["cart"]:
        col1.write(item['item'])
        col2.write(f"{item['quantity']}")
        col3.write(f"${(item['quantity'] * item['price']):.2f}")
        with col4:
            st.button("✏️", key=f"edit_{_SS["cart"].index(item)}",
                      on_click=editProduct, args=(item,_SS["cart"].index(item),))
        with col5:
            st.button("❌", key=f"del_{_SS["cart"].index(item)}", 
                      on_click=removeProduct, args=(item,))

    st.markdown("<hr/>", unsafe_allow_html=True)
    
    (total, discounted_amount, tax, overalltotal) = appfunctions.getCartTotal(_SS["cart"])
    (foot_col1, foot_col2) = st.columns([0.7,0.3], vertical_alignment="center", gap=None, border=False)
    
    foot_col1.markdown(f"##### Total")
    foot_col2.markdown(f"##### ${total:.2f}")
    foot_col1.markdown(f"##### Discount Given")
    foot_col2.markdown(f"##### -${discounted_amount:.2f}")
    foot_col1.markdown(f"##### GST Tax")
    foot_col2.markdown(f"##### +${tax:.2f}")
    foot_col1.markdown(f"### Grand Total")
    foot_col2.markdown(f"### ${overalltotal:.2f}")

    if st.button("Proceed to Checkout", disabled=(len(_SS["cart"])==0)):
        checkout()



