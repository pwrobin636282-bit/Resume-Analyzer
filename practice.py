import streamlit as st

st.title("AI Resume Analyzer")
st.subheader("Upload Your Resume")
st.text("Supported format:PDF")
st.write("Welcome to the Resume Analyzer")

bu=st.button("Analyze resume")
if bu:
    st.write("Submitted Successfully")

ra=st.radio("Pick your choice:",["Student","Working Professional","Fresher"])
if ra:
    st.write(ra)

sl=st.slider("Years of experience", 0,20,1)
if sl:
    st.write(sl)

ti=st.text_input("Enter your name:")
if ti:
    st.write(f"Welcome {ti}. How u doing")

ni=st.number_input("Expected Salary", 3,50)
if ni:
    st.write(f"Your expected salary will be {ni}")

di=st.date_input("Enter your Date of birth")
if di:
    st.write(di)

st.selectbox("Watch the match:",['Portugal','Argentina','Brazil','England'])