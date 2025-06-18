
import streamlit as st
import pandas as pd
import plotly.express as px

# Set wide layout and dark theme
st.set_page_config(layout="wide", page_title="Mental Health Dashboard")

# Apply custom dark theme style
dark_style = '''
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .st-bb, .st-at, .st-af {
        background-color: #0e1117 !important;
    }
    .css-1d391kg, .css-1v3fvcr {
        color: white !important;
    }
    .css-1v0mbdj {
        background-color: #262730;
    }
    </style>
'''
st.markdown(dark_style, unsafe_allow_html=True)

# Title
st.title("🧠 Mental Health in Tech Dashboard")

# Load data
df = pd.read_csv("cleaned_survey.csv")

# Sidebar
st.sidebar.header("🔎 Filter")
gender_filter = st.sidebar.multiselect("Gender", df['Gender'].unique(), default=df['Gender'].unique())
age_range = st.sidebar.slider("Age Range", int(df['Age'].min()), int(df['Age'].max()), (20, 40))
filtered_df = df[(df['Gender'].isin(gender_filter)) & (df['Age'].between(age_range[0], age_range[1]))]

# Row 1: Q1
col1, col2 = st.columns(2)
with col1:
    st.subheader("Treatment Distribution by Age")
    fig1 = px.histogram(filtered_df, x="Age", color="treatment", barmode="group", nbins=20)
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.subheader("Treatment by Gender")
    fig2 = px.histogram(filtered_df, x="Gender", color="treatment", barmode="group")
    st.plotly_chart(fig2, use_container_width=True)

# Row 2: Q2 & part of Q3
col3, col4, col5 = st.columns(3)
with col3:
    st.subheader("Family History vs Treatment")
    fig3 = px.histogram(filtered_df, x="family_history", color="treatment", barmode="group")
    st.plotly_chart(fig3, use_container_width=True)
with col4:
    st.subheader("Benefits Offered")
    fig4 = px.pie(filtered_df, names='benefits')
    st.plotly_chart(fig4, use_container_width=True)
with col5:
    st.subheader("Care Options")
    fig5 = px.pie(filtered_df, names='care_options')
    st.plotly_chart(fig5, use_container_width=True)

# Row 3: Q3 cont. + Q4
col6, col7, col8 = st.columns(3)
with col6:
    st.subheader("Wellness Programs")
    fig6 = px.pie(filtered_df, names='wellness_program')
    st.plotly_chart(fig6, use_container_width=True)
with col7:
    st.subheader("Interference by Company Size")
    fig7 = px.histogram(filtered_df, x="no_employees", color="work_interfere", barmode="group")
    st.plotly_chart(fig7, use_container_width=True)
with col8:
    st.subheader("Interference by Remote Work")
    fig8 = px.histogram(filtered_df, x="remote_work", color="work_interfere", barmode="group")
    st.plotly_chart(fig8, use_container_width=True)

# Row 4: Q5 & Q6
col9, col10, col11 = st.columns(3)
with col9:
    st.subheader("Comfort with Coworkers")
    fig9 = px.histogram(filtered_df, x="coworkers", color="treatment", barmode="group")
    st.plotly_chart(fig9, use_container_width=True)
with col10:
    st.subheader("Comfort with Supervisor")
    fig10 = px.histogram(filtered_df, x="supervisor", color="treatment", barmode="group")
    st.plotly_chart(fig10, use_container_width=True)
with col11:
    st.subheader("Observed Consequences vs Disclosure")
    fig11 = px.histogram(filtered_df, x="obs_consequence", color="treatment", barmode="group")
    st.plotly_chart(fig11, use_container_width=True)
