import streamlit as st

st.title("Personal Info Form")

with st.form("personal_info"):
    st.write("**Enter your details**")

    user_name = st.text_input("Name", key="user_name")
    contact_email = st.text_input("Email", key="contact_email")
    user_age = st.slider("Age", 0, 100, 20, key="user_age")
    user_gender = st.radio(
        "Gender",
        ["Male", "Female", "Other", "Prefer not to say"],
        key="user_gender",
    )

    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("Form submitted!")
    st.write(f"**Name:** {user_name}")
    st.write(f"**Email:** {contact_email}")
    st.write(f"**Age:** {user_age}")
    st.write(f"**Gender:** {user_gender}")
