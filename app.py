import streamlit as st
import numpy as np
import pandas as pd
import joblib
from PIL import Image
import time
model = joblib.load('GBRpipe.joblib')

col1,col2 = st.columns([2,1])
col1.header('*Salary Prediction in 2022*') 
col1.write("Learn More >> [link](https://github.com/Saeedkhazaei)")
photo = Image.open("Salary_P.jpg")
photo.resize((800,600))
col2.image(photo)
st.write("---")

RemoteWrk=('Hybrid', 'Fully remote', 'Fully in-person')

countries = ('Argentina', 'Australia', 'Austria', 'Bangladesh', 'Belgium', 'Brazil', 'Canada', 'China',
            'Czech Republic', 'Denmark', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'India',
            'Indonesia', 'Iran, Islamic Republic of...', 'Ireland', 'Israel', 'Italy', 'Japan', 'Mexico',
            'Netherlands', 'New Zealand', 'Norway', 'Pakistan', 'Poland', 'Portugal', 'Romania',
            'Russian Federation', 'South Africa ', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine',
            'United Kingdom of Great Britain and Northern Ireland', 'United States of America','Other')

education = (
    "Less than a Bachelors",
    "Bachelor’s degree",
    "Master’s degree"
)
OrgSiz=('Just me - I am a freelancer, sole proprietor, etc.','2 to 9 employees','10 to 19 employees',
          '20 to 99 employees', '100 to 499 employees', '500 to 999 employees','1,000 to 4,999 employees',
           '5,000 to 9,999 employees', '10,000 or more employees')

countries1=['United States of America','Other','India', 'Germany', 'United Kingdom of Great Britain and Northern Ireland',
            'Canada','France', 'Brazil', 'Spain', 'Italy','Australia','Netherlands','Poland','Sweden', 'Russian Federation',
            'Turkey', 'Switzerland', 'Israel', 'Austria', 'Pakistan', 'Denmark', 'Iran, Islamic Republic of...', 'Belgium',
            'Norway', 'Portugal', 'Mexico','Greece','Ukraine', 'South Africa ', 'China', 'Czech Republic', 'Bangladesh', 
            'Romania', 'Finland', 'New Zealand', 'Hungary', 'Argentina', 'Japan', 'Ireland', 'Indonesia']
RemoteWork1=['Hybrid', 'Fully remote', 'Fully in-person']
education1=["Less than a Bachelors", "Bachelor’s degree", "Master’s degree"]
OrgSize1=['Just me - I am a freelancer, sole proprietor, etc.','2 to 9 employees','10 to 19 employees',
          '20 to 99 employees', '100 to 499 employees', '500 to 999 employees','1,000 to 4,999 employees',
           '5,000 to 9,999 employees', '10,000 or more employees']
YearsCodePro1=['YearsCodePro']

columns1=countries1+education1+YearsCodePro1+OrgSize1+RemoteWork1

X_old=np.zeros(len(columns1))
X_old_df = pd.DataFrame([X_old], columns = columns1)

country = st.selectbox("Country", countries)
education = st.selectbox("Education Level", education)
expericence = st.slider("Years of Experience", 0, 50, 3)
OrgSize = st.selectbox("THe Size of Your Organization Working in",OrgSiz)
RemoteWork=st.selectbox ("How Do You Work?",RemoteWrk)
X_old_df[country]=1
X_old_df[education]=1
X_old_df[OrgSize]=1
X_old_df[RemoteWork]=1
X_old_df['YearsCodePro']=expericence
ok = st.button("Calculate Salary")
if ok:
    
    salary = model.predict(X_old_df)
    
    st.subheader(f"The estimated salary is ${salary[0]:.2f}")

