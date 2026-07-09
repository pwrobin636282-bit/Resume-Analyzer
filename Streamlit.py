import streamlit as st
st.title("Resume Analyzer")

uploaded_doc=st.file_uploader(
    'Upload Your Resume',
    type=['pdf'])
if uploaded_doc:
    st.success("Resume Uploaded Successfully")

best_match='Data Analyst'
missing = ['Statistics','Tableau','Docker']
Matched_jobs=["Data Analyst",
               "Business Analyst", 
               "Data Scientist",
                "ML Engineer", 
                "Data Engineer"
                ]

bot=st.button("Analyze the resume")
if bot:
    st.metric(
    label="Resume Score",
    value="82%"
    )
    for i,j  in enumerate(Matched_jobs,missing):
        st.write(f"{i}")   
        st.write(f"{j}")