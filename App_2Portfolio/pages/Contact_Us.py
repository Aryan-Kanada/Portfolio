import streamlit as st
from send_email import send_emails

st.header("Contact US")

with st.form(key="contact_forms"):
    user_name = st.text_input("Your Name")
    user_email = st.text_input("Your Email Address")
    user_message = st.text_area("Your Message")
    submit_button = st.form_submit_button("Submit")

    message = f"""Subject:New email form {user_name}
    
    \n\n{user_message}
    
    From: {user_email}
"""

if submit_button:
    send_emails(message)
    st.info("Your Email Was Sent Successfully")