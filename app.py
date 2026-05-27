import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA Dashboard", layout="wide")

# Title
st.title("Exploratory Data Analysis Project")

# Load Dataset
df = pd.read_csv("dataset.csv")

# Show Dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Dataset Info
st.subheader("Dataset Shape")
st.write(df.shape)

# Missing Values
st.subheader("Missing Values")
st.write(df.isnull().sum())

# Statistical Summary
st.subheader("Statistical Summary")
st.write(df.describe())

# Correlation Heatmap
st.subheader("Correlation Heatmap")

corr = df.corr(numeric_only=True)

fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)

st.pyplot(fig)

# Histogram
st.subheader("Histograms")

df.hist(figsize=(12,10))
st.pyplot(plt)

# Boxplot
st.subheader("Boxplot")

fig2, ax2 = plt.subplots(figsize=(10,5))
sns.boxplot(data=df, ax=ax2)

st.pyplot(fig2)

# Insights
st.subheader("Key Insights")

st.write("""
1. Correlation between variables can be observed using heatmap.
2. Histograms show distribution of numerical columns.
3. Boxplots help identify outliers.
4. Statistical summary gives mean, median, std deviation.
""")