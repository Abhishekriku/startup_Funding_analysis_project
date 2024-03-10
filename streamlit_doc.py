import streamlit as st
import pandas as pd
import time

# adding a title
st.title('Startup Dashboard')

# adding a header
st.header("I am learning streamlit")
st.subheader("And I am loving it")

# using write
st.write("This is a normal text")

# using markdown
st.markdown("""
### My Favourite movies
- Shawshank redemption
- Rocky 4
- Matrix
""")

# to display the code
st.code("""
def foo(input):
    return foo**2
x = foo(2)
""")

# to display a latex
st.latex('x^2 + y^2 + 2 = 0')

# displaying a dataframe
df = pd.DataFrame({
    'Name': ['Abhishek', 'Himangshu', 'Amar'],
    'Marks': [60,70,80],
    'Package': [10,12,14]
})
st.dataframe(df)

# Displaying metric
st.metric('Revenue','Rs 3LPA','-3%')

# displaying JSON
st.json({
    'Name': ['Abhishek', 'Himangshu', 'Amar'],
    'Marks': [60,70,80],
    'Package': [10,12,14]
})

# displaying image
st.image('Abhishek.jpg')

# video display
# st.video(' video name')

# adding a sidebar
st.sidebar.title("sidebar ka title")

# adding things in columns side by side
col1, col2 = st.columns(2)
with col1:
    st.image('Abhishek.jpg')
with col2:
    st.image('Abhishek.jpg')

# to display error message
st.error('Login Failed')

st.success("login successful")

st.info("login successful")

st.warning("login successful")

# progress bar
bar = st.progress(0)
for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)

# inputs
email = st.text_input('Enter your Email')
number = st.number_input("Enter age")
st.date_input("Enter registration date")

email = st.text_input("Enter your Email")
password = st.text_input("Enter password")
gender = st.selectbox('Gender',['Male','Female','Others'])
# using buttons for input
btn = st.button("Login Karo")


if btn:
    if email == "abhishek@gmail.com" and password == '1234':
        st.success('Login Successful')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Faile')

file = st.file_uploader('upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())
