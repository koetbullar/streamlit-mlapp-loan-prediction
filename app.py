import streamlit as st

#streamlit run app.py
st.title("Streamlit Demo")

st.header("Header of my app")

st.subheader("Sub- Header of my app")

st.text("This is an example text")

st.success("Success message")
st.warning("This is a warning")
st.info("This is an information")
st.error("ERROR!")

if st.checkbox("Select/Unselect"):
    st.text("User selected the checkbox")
else:
    st.text("User has not selected the checkbox")

state = st.radio("What is your favourite color?", ("Red", "Green", "Yellow"))

if state == "Green":
    st.text("Color chosen was Green")

occupation = st.selectbox("What is your occupation?", ("Student", "Vlogger", "Engineer"))

st.text(f"Selected occupation is: {occupation}")

if st.button("Example button"):
    st.info("You clicked the button")

st.sidebar.header("Heading of sidebar")
st.sidebar.text("Created by Patryk")
