import streamlit as st
import mylibrary

st.write("Hello!")
st.text_input("Enter the quantity of African Oranges $2 each", key="oranges")
st.number_input("Enter the quantity of Fuji Apples $3 each", min_value=0, max_value=10, step=1, key="apples")
st.slider("How many plastic bags do you want", min_value=0, max_value=3, step=1, key="bags")
bags_cost = mylibrary.plastic_bags_price(st.session_state.bags)
st.write("Your plastic bags will cost $" + str(bags_cost))

if st.button('Get Total'):
    st.write('Calculating Your Total ...')
    oranges = int(st.session_state.oranges)
    apples = int(st.session_state.apples)
    result = mylibrary.calculate_total(oranges, apples)
    total = bags_cost + result
    st.write('Please pay {:.2f}'.format(total))
else:
    st.write('Please Key In The Quantity')