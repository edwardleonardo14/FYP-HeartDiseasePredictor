import streamlit as st

st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="⚕"
)

with st.container():
    st.subheader("FYP Project Deployment")
    st.title("Data Analysis and Predictive Modelling on Heart Disease based on People’s Lifestyle 🧡")
    st.write("Edward Leonardo | TP058284 | APU3F2211CS(DA)")
    st.write("This Project is part of the requirement to gain a bachelor degree of B.Sc. (Hons) Computer Science Specialism in Data Analytics from Asia Pacific University of Technology and Innovation.")
    
st.write("---")
# Explanation of the project
st.write("""
## Project Description 📑

This project's aim is to increase awareness regarding on what Lifesytle Choices or Personal Key Indicators (PKIs) that can leads to Coronary Artery Disease, and using the Prediction Machine available to predict their likelihood based on their current general condition.
With this, the hope is to raise awareness of the population regarding the danger of Coronary Artery Disease (CAD) Type of Heart Disease, and what factors that have a big impact towards it.
         
**THIS PROJECT IS CREATED ONLY FOR EDUCATIONAL PURPOSES, AND NOT MEANT TO REPLACE A PROFESSIONAL CONSULTATION/TREATMENT.**
         
This results of this project can be divided into Three parts:

1. A Predictive Machine Learning Model that can be used to predict the likelihood of a person having a Coronary Artery Disease based on the various lifestyle choices.

2. An Exploratory Data Analysis (EDA) result, using Visualization to be used as an informational tool that can be shared.
         
3. A Web Application Deployment that contains both the results above, to allow easier usability by the large population.

""")

st.write("---")

st.write("""
## Project Outcome ✅

1. A Gradient Boost Machine Learning Model with 74% Accuracy and 78% Recall.

2. Visualizations representing the correlation between the features and the target variable.
         
3. A Web Application that can shows and utilize both results above.

""")

# st.write("---")

# st.write("""
# ## Learn More 🤓
# To Learn More about the Project, Click the links below

# 1. [Project Report in PDF](link-to-project-report-pdf)

# 2. [GitHub Repository of the Project](https://github.com/edwardleonardo14/FYP-HeartDiseasePredictor)
# """)

st.write("---")

st.write("""
## Contact Me 📧
Contact me through:

1. [LinkedIn](https://www.linkedin.com/in/edwardleonardo/)

2. [University Email](mailto:{TP058284@mail.apu.edu.my})
         
3. [Personal Email](mailto:{edwardleonardo14@gmail.com})
""")