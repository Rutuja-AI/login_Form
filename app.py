import streamlit as st

# Dictionary containing email and password pairs
users = {'morepurva@gmail.com': '12345', 'pranjalsutar@gmail.com': '12345', 'rutuja': '12345'}

# Input fields for email and password
email = st.text_input('Enter email:')
password = st.text_input('Enter password:', type='password')

# Login button
btn = st.button('Login')

# Authentication logic
if btn:
    if email in users and password == users[email]:
        st.success('Login Successful!')
        st.balloons()
    else:
        st.error('Login Error: Invalid email or password')
