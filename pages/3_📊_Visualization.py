import streamlit as st
# Data Manipulation
import pandas as pd
import numpy as np
import re

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale = 2)
import missingno as msno
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

st.set_page_config(
    page_title = "Visualization",
    page_icon = "📊"
)

with st.container():
    st.subheader("FYP Project Deployment")
    st.title("Visualization 📊")
    st.write("This is the Visualization page. User can check the correlation between Heart Disease and the chosen Lifestyle Factors. Explanation will also be provided.")

fullData = pd.read_csv("fullDataVisualization.csv")

sns.set(style="darkgrid")
sns.set(rc={'figure.figsize': (16, 8)})

choices = [
    "Age Category",
    "BMI",
    "Diabetic",  
    "Smoking", 
    "Alcohol Drinking", 
    "Stroke", 
    "Physical Health",
    "Mental Health", 
    "Difficulty Walking", 
    "Gender", 
    "Physical Activity",
    "Sleep Time", 
    "Asthma", 
    "Kidney Disease", 
    "Skin Cancer",
    "Race", 
    "General Health"
]

selected_choice = st.selectbox("Select an option:", choices)

selected_choice = selected_choice.replace("Gender", "Sex")
selected_choice = selected_choice.replace("Difficulty Walking", "DiffWalking")
selected_choice = selected_choice.replace("General Health", "GenHealth")

selected_choice = selected_choice.replace(" ", "")

if selected_choice in ["BMI", "SleepTime", "PhysicalHealth", "MentalHealth"]:
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05)

    heartDiseaseBMI = fullData.loc[fullData['HeartDisease'] == 1, selected_choice]
    noHeartDiseaseBMI = fullData.loc[fullData['HeartDisease'] == 0, selected_choice]

    boxplot_trace_1 = go.Box(x=heartDiseaseBMI, name='Heart Disease', marker=dict(color="#E67373"), orientation='h')
    boxplot_trace_2 = go.Box(x=noHeartDiseaseBMI, name='No Heart Disease', marker=dict(color='#7373E6'), orientation='h')

    histogram_trace_1 = go.Histogram(x=heartDiseaseBMI, name='Heart Disease', marker=dict(color="#E67373"), opacity=0.7, histnorm='probability density', nbinsx=50)
    histogram_trace_2 = go.Histogram(x=noHeartDiseaseBMI, name='No Heart Disease', marker=dict(color='#7373E6'), opacity=0.7, histnorm='probability density', nbinsx=50)

    fig.add_trace(boxplot_trace_1, row=1, col=1)
    fig.add_trace(boxplot_trace_2, row=2, col=1)

    fig.add_trace(histogram_trace_1, row=3, col=1)
    fig.add_trace(histogram_trace_2, row=3, col=1)

    fig.update_layout(
        title=f"Correlation between Heart Disease and {selected_choice}",
        showlegend=False,
        height=600,
        width=800,
        barmode='overlay'
    )
    st.plotly_chart(fig)
else:
    if selected_choice == "GenHealth":
        genhealth_order = ["Excellent", "Very good", "Good", "Fair", "Poor"]
        correlation_counts = fullData.groupby([selected_choice, "HeartDisease"]).size().unstack().reindex(genhealth_order)
        xaxis_tickvals = genhealth_order
        xaxis_ticktext = genhealth_order
    elif selected_choice == "Race":
        race_order = ["White", "Asian", "Black", "Hispanic", "American Indian/Alaskan Native", "Other"]
        correlation_counts = fullData.groupby([selected_choice, "HeartDisease"]).size().unstack().reindex(race_order)
        xaxis_tickvals = race_order
        xaxis_ticktext = race_order
    elif selected_choice == "Diabetic":
        diabetic_order = ["Yes", "Yes (during pregnancy)", "No", "No, borderline diabetes"]
        correlation_counts = fullData.groupby([selected_choice, "HeartDisease"]).size().unstack().reindex(diabetic_order)
        xaxis_tickvals = diabetic_order
        xaxis_ticktext = diabetic_order
    elif selected_choice == "AgeCategory":
        agecategory_order = ["18-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80 or older"]
        correlation_counts = fullData.groupby([selected_choice, "HeartDisease"]).size().unstack().reindex(agecategory_order)
        xaxis_tickvals = agecategory_order
        xaxis_ticktext = agecategory_order
    else:
        desired_order = [1, 0]
        correlation_counts = fullData.groupby([selected_choice, "HeartDisease"]).size().unstack().reindex(desired_order)
        xaxis_tickvals = desired_order
        if selected_choice == "Sex":
            xaxis_ticktext = ["Male", "Female"]
        else:
            xaxis_ticktext = ["Yes", "No"]

    yes_trace = go.Bar(
        x=xaxis_tickvals,
        y=correlation_counts[1],
        name='Heart Disease',
        marker=dict(color='rgba(230, 115, 115, 0.7)')
    )

    no_trace = go.Bar(
        x=xaxis_tickvals,
        y=correlation_counts[0],
        name='No Heart Disease',
        marker=dict(color='rgba(115, 115, 230, 0.7)')
    )

    layout = go.Layout(
        title=f"Grouped Bar Chart of Heart Disease by {selected_choice}",
        xaxis=dict(
            title=selected_choice,
            tickvals=xaxis_tickvals,
            ticktext=xaxis_ticktext
        ),
        yaxis=dict(title='Count'),
        barmode='group'
    )

    data = [yes_trace, no_trace]

    fig = go.Figure(data=data, layout=layout)

    st.plotly_chart(fig)

if selected_choice == "BMI":
    st.write("""
## BMI

Body Mass Index (BMI) is a measurement unit of a Person's mass.
BMI can be calculated using a person's weight divided by the square of the person's height (Kilogram/Meters^2).
             
BMI can be used for a health screnning, as high BMI can indicate high amount of fat in the body. A normal BMI range should be between 18.5-25,
where anything under can be considered as underweight, while anything above can be considered as overweight/obese.

**From the Charts above, It shows that people with Coronary Artery Disease (CAD) have a higher BMI number overall.
Having a BMI in the normal range is one of the best way of to reduce the risk of CAD.**
         
[Learn More](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html)

""")
elif selected_choice == "AgeCategory":
    st.write("""
## Age Category

Age Category covers the grouping for the age of a human.

**From the Charts above, It shows that a person risk of having a Coronary Artery Disease (CAD) is becoming higher
as they age. Since aging is unavoidable, an older individual can reduce their risk by fixing their other lifestyle habits.**
  
[Learn More](https://www.nia.nih.gov/health/heart-health-and-aging)

""")
elif selected_choice == "Diabetic":
    st.write("""
## Diabetic

Diabetes is a chronic health condition where your body does not produce enough insulin, causing too much sugar stays in a person's bloodstream.
Diabetes can cause Coronary Artery Disease (CAD) due to the high blood sugar can causes damages to blood vessels and artery walls, causing CAD.

**From the Chart above, a person with diabetes or borderline diabetes (prediabetes) have a very high chance to have a CAD also.
Diabetes can be prevented by a healthier lifestyle changes, such as lowering your weight and being more physically active.**
      
[Learn More](https://www.cdc.gov/diabetes/library/features/diabetes-and-heart.html)

""")
elif selected_choice == "Smoking":
    st.write("""
## Smoking

Someone can be considered a smoker when they have already smoked 100 cigarettes in their entire life.
Smoking can cause Coronary Artery Disease due to the chemical inside the cigarette that can cause the blood vessels to become swollen/inflamed,
causing the narrowing of the blood vessels, which putting more stress to the heart, which may damages it.

**From the chart above, a person that smokes have a higher chance of having a CAD.
The best way to reduce the damages is to immediately stop smoking. Otherwise, start a more healthier lifestyle can also mitigate some of the damages.**
      
[Learn More](https://www.cdc.gov/tobacco/sgr/50th-anniversary/pdfs/fs_smoking_cvd_508.pdf)

""")
elif selected_choice == "AlcoholDrinking":
    st.write("""
## Alcohol Drinking

Drinking excessive amounts of Alcohol can cause high blood pressure, that can put a higher pressure towards the arteries and blood vessels.
The increased level of stress on the arteries and blood vessels can causes Coronary Artery Disease (CAD).

**From the chart above, it shows that Drinking Alcohol did not have a big impact towards the risk of CAD. But the effect of drinking alcohol excessively
may happen over a longer period of time. Stop/regulate alcohol consumption still can reduce the damages towards the blood vessels and arteries.**
      
[Learn More](https://alcoholthinkagain.com.au/alcohol-and-your-health/long-term-health-effects)

""")
elif selected_choice == "Stroke":
    st.write("""
## Stroke

Stroke is one of the major side-effect from Coronary Artery Disease (CAD). This is caused by the lack of oxygen-rich blood flow to the brain.
Stroke also can causes a heart disease, since studies shows that Stroke patient have a higher chance of getting a cardiac problem also.

**From the chart above, it shows that if a person have a CAD, they are also more likely to get a stroke.
Individual that only have stroke also have a higher chance to have a cardiac problem in the future.**
      
[Learn More](https://www.cdc.gov/stroke/risk_factors.htm)

""")
elif selected_choice == "PhysicalHealth":
    st.write("""
## Physical Health

Physical Health also have an effect towards the risk of Coronary Artery Disease (CAD). Someone with bad physical health means that they may suffering from
a chronic disease, or is currently living an unhealthy lifestlye.

**From the chart above, it shows that someone that experience a lot of bad physical health/sickness have a higher chance of suffering from
CAD.**

""")
elif selected_choice == "MentalHealth":
    st.write("""
## Mental Health

Mental Health can have a long-term effect that can cause a chronic disease, such as Coronary Artery Disease (CAD).

**From the chart above, it shows that individual with bad mental health may have a higher chance of suffering from CAD.**
      
[Learn More](https://www.cdc.gov/heartdisease/mentalhealth.htm)

""")
elif selected_choice == "DiffWalking":
    st.write("""
## Difficulty Walking

Difficulty Walking can be a non-direct cause of Coronary Artery Disease (CAD). Maybe due to other health problems, but Difficulty Walking or Climbing Stair
Individuals may have a more difficult time to do physical activity.

**From the chart above, it shows that people with Difficulty Walking have a high risk of developing CAD also.**
      
[Learn More](https://www.cdc.gov/heartdisease/risk_factors.htm)

""")
elif selected_choice == "Sex":
    st.write("""
## Gender

Gender may have an effect towards the risk of Coronary Artery Disease (CAD). This can be due to Hormones differences, Cholestrol buildup, different body fat location,
and stress.

**From the chart above, it shows that Male have a higher risk of CAD compared to Female.**
      
[Learn More](https://www.louisianaheart.org/blog/do-men-have-a-higher-risk-for-heart-disease#:~:text=That%20said%2C%20men%20have%20larger,found%20in%20smaller%20blood%20vessels.)

""")
elif selected_choice == "PhysicalActivity":
    st.write("""
## Physical Activity

Physical Activity is one of the most commont way known to reduce the risk of Coronary Artery Disease. Physical Activity can be in a form of Sports or normal Exercise.
It is recommended for adults to get 2.5 hours of physical exercise per week, and 1 hour for children/adolescents.

**From the chart above, it shows that people that does Physical Activity has a lower risk of CAD.**
      
[Learn More](https://www.nhs.uk/conditions/coronary-heart-disease/prevention/)

""")
elif selected_choice == "SleepTime":
    st.write("""
## Sleep Time

Sleep amount per day may not have a big effect towards Coronary Artery Disease (CAD) directly, but sleeping disorder, such as insomnia, is linked to causes
high blood pressure, high stress level, and unhealtier lifestyle in a long-term, which are risk factors that can causes CAD.

**From the chart above, Sleep Amount cannot be definitely identified as a risk factors towards CAD. But, due to the long-term effect, a healthy, 7-9 hours of sleep
each day is recommended**
      
[Learn More](http://www.eurekaselect.com/article/15831)

""")
elif selected_choice == "Asthma":
    st.write("""
## Asthma

Asthma may not directly caused Coronary Artery Disease (CAD), but Asthma is still known to causes inflammatories all around the body, including the blood vessels.
This inflammation may causes a long-term damages towards the blood vessels, thus increasing the risk of High Blood Pressure, leading to CAD.

**From the chart above, It shows that people with Asthma has a higher risk of CAD.**
      
[Learn More](https://www.healthcentral.com/condition/asthma/how-asthma-and-heart-disease-are-connected)

""")
elif selected_choice == "KidneyDisease":
    st.write("""
## Kidney Disease

Kidney Disease is known to boost the risk factors of Coronary Artery Disease (CAD). This includes diabetes, hypertension, and inflammation.

**From the chart above, it shows that people with Kidney Disease has a higher risk of CAD.**
      
[Learn More](https://linkinghub.elsevier.com/retrieve/pii/S0735109719373905)

""")
elif selected_choice == "SkinCancer":
    st.write("""
## Skin Cancer

Skin Cancer may not directly be the cause of Coronary Artery Disease (CAD), but the tumor that is associated with Skin Cancer can spread around through metastatis
to other internal organ, such as the Heart, which can causes Heart Diseases such as Arrhythmia and Heart Failure.

**From the chart above, it shows that people with Skin Cancer has a slightly higher risk of CAD.**
      
[Learn More]()

""")
elif selected_choice == "Race":
    st.write("""
## Race

Race may have an effect towards Coronary Artery Disease (CAD). This can be caused due to cultural differences, lifestyle differences, and higher risks towards
specific risk factors. Social problems such as ethnicity or racism can also cause higher stress level. All of these factors are depedant on where the Person live,
and how the culture they grew up in.
      
[Learn More](https://www.ahajournals.org/doi/full/10.1161/CIRCOUTCOMES.121.007917#:~:text=Black%20adults%20experience%20higher%20burden,CVD%2C%20relative%20to%20White%20adults.&text=Similarly%2C%20American%20Indian%20individuals%20are,compared%20with%20the%20White%20population.)

""")
elif selected_choice == "GenHealth":
    st.write("""
## General Health

General Health is one of the indicators a person can use to measure their current health status. As your general health condition worsen, your risk of Coronary Artery
Disease (CAD) may increases as well.

**From the chart above, it shows that as people's general health worsen, their risk of CAD will get higher.**

""")