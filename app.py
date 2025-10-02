import streamlit as st
import mylibrary
import products

products_instance = products.products()
# Mock data for demonstration purposes
products_instance.items = [{"name": "Sample Product", "details": "This is a sample product.", "price": 10, "image": "./images/image1.png"}, 
                                {"name": "Another Product", "details": "This is another product.", "price": 15, "image": "./images/image2.png"},
                                {"name": "Third Product", "details": "This is the third product.", "price": 20, "image": "./images/image3.png"},
                                {"name": "Fourth Product", "details": "This is the fourth product.", "price": 25, "image": "./images/image4.png"},
                                {"name": "Fifth Product", "details": "This is the fifth product.", "price": 30, "image": "./images/image5.png"},
                                {"name": "Sixth Product", "details": "This is the sixth product.", "price": 35, "image": "./images/image6.png"},
                                {"name": "Seventh Product", "details": "This is the seventh product.", "price": 40, "image": "./images/image7.png"},
                                {"name": "Eighth Product", "details": "This is the eighth product.", "price": 45, "image": "./images/image8.png"},
                                {"name": "Ninth Product", "details": "This is the ninth product.", "price": 50, "image": "./images/image9.png"},
                                {"name": "Tenth Product", "details": "This is the tenth product.", "price": 55, "image": "./images/image10.png"}]

#list products


def onClick():
    st.write("You have clicked a product!")

st.write("We have the following products:")

for i in range(0,len(products_instance.items),2):
    col1, col2 = st.columns(2, vertical_alignment="center")
    with col1:
        st.text(f"- {products_instance.items[i]['name']}: {products_instance.items[i]['details']}")
        st.image(products_instance.items[i]["image"])
        # st.text("pretend this is an image")
        st.button(f"Buy", key=f"button_{i}", on_click=onClick)
    with col2:
        # st.text("pretend this is an image")
        st.text(f"- {products_instance.items[i+1]['name']}: {products_instance.items[i+1]['details']}")
        st.image(products_instance.items[i+1]["image"])
        st.button(f"Buy", key=f"button_{i+1}", on_click=onClick)
    

#col1, col2 = st.columns(2, vertical_alignment="center")

#with col1:
    # st.header("Select")
# with col2:
    # st.header("Product Details")
# for i in range(len(products_instance.items)):
#     st.columns(1)[0].button(f"Select", key=f"button_{i}", on_click=onClick)
#     st.columns(2)[0].text(f"- {products_instance.items[i]['name']}: {products_instance.items[i]['details']}")
    # st.image(products_instance.items[i]["image"])
    # st.write(f"- {products_instance.items[i]['name']}: {products_instance.items[i]['details']}")

# st.write("Hello!")
# st.text_input("Enter the quantity of African Oranges $2 each", key="oranges")
# st.number_input("Enter the quantity of Fuji Apples $3 each", min_value=0, max_value=10, step=1, key="apples")
# st.slider("How many plastic bags do you want", min_value=0, max_value=3, step=1, key="bags")
# bags_cost = mylibrary.plastic_bags_price(st.session_state.bags)
# st.write("Your plastic bags will cost $" + str(bags_cost))


    
# products_instance = products.products()
# st.write("We have the following products:")
# for item in products_instance.list_products():
#     st.image("./images/image.png")
#     st.button(f"- {item['name']}: {item['details']}", on_click=onClick)
    
    
# if st.button('Get Total'):
#     st.write('Calculating Your Total ...')
#     oranges = int(st.session_state.oranges)
#     apples = int(st.session_state.apples)
#     result = mylibrary.calculate_total(oranges, apples)
#     total = bags_cost + result
#     st.write('Please pay {:.2f}'.format(total))
# else:
#     st.write('Please Key In The Quantity')