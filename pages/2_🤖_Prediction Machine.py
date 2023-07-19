import streamlit as st
# Data Manipulation
import pandas as pd
import numpy as np
import re
import pickle

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale = 2)
import missingno as msno

from sklearn.preprocessing import MinMaxScaler

st.set_page_config(
    page_title = "Prediction Machine",
    page_icon = "🤖"
)

with st.container():
    st.subheader("FYP Project Deployment")
    st.title("Prediction Machine 🤖")
    st.write("""This is the Predictive Machine Learning Model. User can put in their data below, and click on "Predict" button to use the Machine Learning Model.""")

st.write("---")
st.write("## User Input 📋")
gender = st.selectbox("Select your gender", ["Male", "Female"])
race = st.selectbox("Select your Ethnicity", ['Asian','Caucassian/White','African/Black','Hispanic','American Indian/Alaskan Native','Other'])
age = st.slider("Select your Age", 18, 120)

col1, col2 = st.columns([3,1])

with col1:
    height = st.number_input("Enter your body height", min_value=0.0)
    weight = st.number_input("Enter your body weight", min_value=0.0)

with col2:
    heightUnit = st.selectbox("Height's unit", ["Centimeter", "Meter"])
    weightUnit = st.selectbox("Weight's unit", ["Kilogram", "Pounds"])

sleepTime = st.slider("In 24 Hours/a day, how long do you usually sleep for?", 0, 24)
genHealth = st.select_slider("How would you consider your current General Health?", ['Poor','Fair','Good','Very good','Excellent'])
physicalHealth = st.slider("How many days during the past 30 days you are experiencing bad physical health?", 0, 30)
mentalHealth = st.slider("How many days during the past 30 days you are experiencing bad mental health?", 0, 30)

col1, col2 = st.columns(2)
with col1:
    smoking = st.radio("Have you ever smoked 100 Cigarettes in your entire life?", ("Yes", "No"))
    diffWalking = st.radio("Do you have difficulty walking or climbing stairs?", ("Yes", "No"))
    skinCancer = st.radio("Have you ever had/are you currently suffering from Skin Cancer?", ("Yes","No"))
    diabetic = st.radio("Have you ever had/are you currently suffering from diabetes?)", ("Yes","Yes (during pregnancy)","No", "No, borderline diabetes"))
with col2:
    stroke = st.radio("Have you ever suffered from a stroke?", ("Yes","No"))
    asthma = st.radio("Have you ever had/are you currently suffering from Asthma?", ("Yes","No"))
    kidneyDisease = st.radio("Have you ever had/are you currently suffering from Kidney Disease?", ("Yes","No"))
    physicalActivity = st.radio("Are you physically active? Like Exercising or Sports", ("Yes","No"))

alcohol = st.radio("Have you consider/Do you consider yourself a heavy alcohol drinker? (Adult Male more than 14 alcohol drinks per week, Adult Female more than 7 alcohol drinks per week)", ("Yes", "No"))

if st.button("Predict"):
    if height and weight:
        gender = 1 if gender == 'Male' else 0

        raceAsian = 1 if race == 'Asian' else 0
        raceWhite = 1 if race == "Caucassian/White" else 0
        raceBlack = 1 if race == "African/Black" else 0
        raceHispanic = 1 if race == "Hispanic" else 0
        raceNative = 1 if race == "American Indian/Alaskan Native" else 0
        raceOther = 1 if race == "Other" else 0

        ageCategory1824 = 1 if 18 <= age <= 24 else 0
        ageCategory2529 = 1 if 25 <= age <= 29 else 0
        ageCategory3034 = 1 if 30 <= age <= 34 else 0
        ageCategory3539 = 1 if 35 <= age <= 39 else 0
        ageCategory4044 = 1 if 40 <= age <= 44 else 0
        ageCategory4549 = 1 if 45 <= age <= 49 else 0
        ageCategory5054 = 1 if 50 <= age <= 54 else 0
        ageCategory5559 = 1 if 55 <= age <= 59 else 0
        ageCategory6064 = 1 if 60 <= age <= 64 else 0
        ageCategory6569 = 1 if 65 <= age <= 69 else 0
        ageCategory7074 = 1 if 70 <= age <= 74 else 0
        ageCategory7579 = 1 if 75 <= age <= 79 else 0
        ageCategory80old = 1 if 80 <= age <= 120 else 0

        if heightUnit == "Centimeter":
            height = height/100
            height = round(height, 2)
        if weightUnit == "Pounds":
            weight *= 0.45359237
            weight = round(weight, 2)
        BMI = weight/(height ** 2)
        BMI = round(BMI, 2)

        genHealthPoor = 1 if genHealth == "Poor" else 0
        genHealthFair = 1 if genHealth == "Fair" else 0
        genHealthGood = 1 if genHealth == "Good" else 0
        genHealthVeryGood = 1 if genHealth == "Very good" else 0
        genHealthExcellent = 1 if genHealth == "Excellent" else 0

        diabeticYes = 1 if diabetic == "Yes" else 0
        diabeticYesBut = 1 if diabetic == "Yes (during pregnancy)" else 0
        diabeticNo = 1 if diabetic == "No" else 0
        diabeticNoBut = 1 if diabetic == "No, borderline diabetes" else 0        

        skinCancer = 1 if skinCancer == 'Yes' else 0
        smoking = 1 if smoking == 'Yes' else 0
        alcohol = 1 if alcohol == 'Yes' else 0
        stroke = 1 if stroke == 'Yes' else 0
        diffWalking = 1 if diffWalking == 'Yes' else 0
        asthma = 1 if asthma == 'Yes' else 0
        kidneyDisease = 1 if kidneyDisease == 'Yes' else 0
        physicalActivity = 1 if physicalActivity == 'Yes' else 0

        if diabeticYesBut == 1 and gender == 1:
            st.warning("You cannot be a Male and have a Pregnancy-caused Diabetes!")
            st.stop()

        data = {'BMI': BMI,
                'Smoking': smoking,
                'AlcoholDrinking': alcohol,
                'Stroke': stroke,
                'PhysicalHealth': float(physicalHealth),
                'MentalHealth': float(mentalHealth),
                'DiffWalking': diffWalking,
                'Sex': gender,
                'PhysicalActivity': physicalActivity,
                'SleepTime': float(sleepTime),
                'Asthma': asthma,
                'KidneyDisease': kidneyDisease,
                'SkinCancer': skinCancer,
                'AgeCategory_18-24': ageCategory1824,
                'AgeCategory_25-29': ageCategory2529,
                'AgeCategory_30-34': ageCategory3034,
                'AgeCategory_35-39': ageCategory3539,
                'AgeCategory_40-44': ageCategory4044,
                'AgeCategory_45-49': ageCategory4549,
                'AgeCategory_50-54': ageCategory5054,
                'AgeCategory_55-59': ageCategory5559,
                'AgeCategory_60-64': ageCategory6064,
                'AgeCategory_65-69': ageCategory6569,
                'AgeCategory_70-74': ageCategory7074,
                'AgeCategory_75-79': ageCategory7579,
                'AgeCategory_80 or older': ageCategory80old,
                'Race_American Indian/Alaskan Native': raceNative,
                'Race_Asian': raceAsian,
                'Race_Black': raceBlack,
                'Race_Hispanic': raceHispanic,
                'Race_Other': raceOther,
                'Race_White': raceWhite,
                'Diabetic_No': diabeticNo,
                'Diabetic_No, borderline diabetes': diabeticNoBut,
                'Diabetic_Yes': diabeticYes,
                'Diabetic_Yes (during pregnancy)': diabeticYesBut,
                'GenHealth_Excellent': genHealthExcellent,
                'GenHealth_Fair': genHealthFair,
                'GenHealth_Good': genHealthGood,
                'GenHealth_Poor': genHealthPoor,
                'GenHealth_Very good': genHealthVeryGood,
                }
        input = pd.DataFrame(data, index = [0])

        with open('scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
        input_scaled = scaler.transform(input)
        # st.write(input)
        # st.write(input_scaled)
        with open('GradientBoost.pkl', 'rb') as f:
            model = pickle.load(f)

        prediction = model.predict(input)
        prediction_prob = model.predict_proba(input)
        probability = round(prediction_prob[0][1] * 100, 2)
        # st.write("Confidence rate (%):", prediction_prob)
        # st.write("Prediction: ", prediction)
        st.write(f"## The probability that you'll suffer from a"
                 f" Coronary Artery Disease is {probability}%.")
        if probability <= 15:
            st.write("**Stay healthy!🏃‍♀️**")
        elif probability >= 15 and probability <= 40:
            st.write("**Try to implement a better lifestyle to lower the risk!🥗**")
        elif probability >= 41 and probability <= 75:
            st.write("**Uh oh. Implement a better lifestyle and do consult a medical professional!🏥**")
        elif probability > 75:
            st.write("**Do a consultation with a medical professional immediately!👨‍⚕️**")

        if age >= 18 and age <= 34:
            st.write("---")
            input['AgeCategory_18-24'] = 0
            input['AgeCategory_25-29'] = 0
            input['AgeCategory_30-34'] = 0
            input['AgeCategory_35-39'] = 0
            input['AgeCategory_55-59'] = 1
            input_scaled = scaler.transform(input)
            prediction_prob = model.predict_proba(input)
            probability = round(prediction_prob[0][1] * 100, 2)
            if probability > 40:
                st.write(f"## But, by the time you are 50, if you did not change your lifestyle, your risk of suffering from Coronary Artery disease is {probability}%!")
            else:
                st.write(f"## But, by the time you are 50, if you did not change your lifestyle, your risk of suffering from Coronary Artery disease is {probability}%.")

        st.write("---")

        st.write("## Recommendation based on your data:")
        if BMI < 18.5:
            st.write(f"- Try increasing your **Body Weight** to reach a healthier BMI. Your BMI is **{BMI}**, a healthy range of BMI is **18.5-25.**")
        if BMI > 25:
            st.write(f"- Try decreasing your **Body Weight** to reach a healthier BMI. Your BMI is **{BMI}**, a healthy range of BMI is **18.5-25.**")
        if sleepTime < 7:
            st.write("- Try increasing your **Sleep Time** Amount. Recommended amount is 7-9 Hours per day.")
        if genHealthGood or genHealthFair or genHealthPoor:
            st.write("- Try to improve your **General Health** to by living a more healthier lifestyle.")
        if physicalHealth >= 10:
            st.write("- Try to consult to a medical professional regarding your **Physical Health** problem.")
        if mentalHealth >= 10:
            st.write("- Try to consult to a Psychologist regarding your **Mental Health** problem.")
        if smoking:
            st.write("- Try to reduce or stop your **Smoking**.")
        if diffWalking:
            st.write("- Try to consult a medical professional if you have **Difficulty Walking**.")
        if diabeticYes or diabeticNoBut:
            st.write("- For **Diabetes**, consult a medical professional and try to have a healthier lifestyle.")
        if diabeticYesBut:
            st.write("- For **Diabetes due to Pregnancy**, consult a medical professional and try to have a healthier lifestyle after giving birth.")
        if physicalActivity == 0:
            st.write("- Try to increase your **Physical Activity** amount by Exercising or doing Sports.")
        if alcohol:
            st.write("- Try to limit or stop **Drinking Alcohol.**")
        elif (BMI >= 18.5 and BMI <= 25) and sleepTime >= 7 and (genHealthVeryGood or genHealthExcellent) and physicalActivity and physicalHealth < 10 and mentalHealth < 10 and smoking == 0 and diffWalking == 0 and diabeticNo and alcohol == 0:
            st.write("- Nothing here. Keep up your healthy lifestyle!")

    else:
        st.warning("Please enter all data.")
