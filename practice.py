import streamlit as st
from resume_analyzer import analyze_resume

st.title("AI Resume Analyzer")
st.subheader("Upload Your Resume")
st.text("Supported format:PDF")
st.write("Welcome to the Resume Analyzer")

ra=st.radio("Pick your choice:",["None","Student","Working Professional","Fresher"])
if ra:
    st.write(ra)

sl=st.slider("Years of experience", 0,20,0)
if sl:
    st.write(sl)

ti=st.text_input("Enter your name:")
if ti:
    st.write(f"Welcome {ti}. How u doing")

ni=st.number_input("Expected Salary", 1,50)
if ni:
    st.write(f"Your expected salary will be {ni}")

di=st.date_input("Enter your Date of birth")
if di:
    st.write(di)

chu=st.file_uploader("Uplaod your Resume",type=['pdf'])
bu=st.button("Analyze resume")
if bu:
    if chu:
        resume_path=f"resumes/{chu.name}"
        with open(resume_path, "wb") as f:
            f.write(chu.getbuffer())
        st.success("Submitted Successfully")
        result_df = analyze_resume(resume_path)
        st.dataframe(result_df)
    else:
        st.write("Please upload a resume")



