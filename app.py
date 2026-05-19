import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# PAGE TITLE
st.title("AI Customer Experience Intelligence Dashboard")

st.subheader("Restaurant Behavioral Analytics")

# LOAD FILES
analytics_df = pd.read_csv("analytics.csv")
dwell_df = pd.read_csv("dwell_time.csv")

# KPI CALCULATIONS
average_crowd = analytics_df["People"].mean()
peak_crowd = analytics_df["People"].max()
average_dwell = dwell_df["Estimated_Dwell_Time"].mean()

# KPI DISPLAY
col1, col2, col3 = st.columns(3)

col1.metric("Average Crowd", round(average_crowd,2))
col2.metric("Peak Crowd", peak_crowd)
col3.metric("Avg Dwell Time", round(average_dwell,2))

# CROWD TREND GRAPH
st.subheader("Crowd Trend Analysis")

fig1, ax1 = plt.subplots(figsize=(10,4))

ax1.plot(
    analytics_df["Frame"],
    analytics_df["People"],
    linewidth=3
)

ax1.set_xlabel("Frame")
ax1.set_ylabel("People Count")

st.pyplot(fig1)

# DWELL TIME GRAPH
st.subheader("Customer Dwell Time")

fig2, ax2 = plt.subplots(figsize=(10,4))

ax2.bar(
    dwell_df["Person_ID"].astype(str),
    dwell_df["Estimated_Dwell_Time"]
)

ax2.set_xlabel("Person ID")
ax2.set_ylabel("Seconds")

st.pyplot(fig2)

# RAW DATA
st.subheader("Raw Analytics Data")
st.dataframe(analytics_df)

st.subheader("Dwell Time Data")
st.dataframe(dwell_df)
