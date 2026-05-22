import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# PAGE CONFIGURATION
st.set_page_config(
    page_title="VisionIQ Analytics",
    layout="wide"
)

# DARK THEME STYLING
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

div[data-testid="metric-container"] {
    background-color: #1E1E1E;
    border: 1px solid #333333;
    padding: 20px;
    border-radius: 12px;
}

h1, h2, h3 {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.title("VisionIQ Analytics")

st.subheader("AI Customer Experience Intelligence Platform")

# LOAD CSV FILES
analytics_df = pd.read_csv("analytics.csv")
dwell_df = pd.read_csv("dwell_time.csv")

# KPI CALCULATIONS
average_crowd = analytics_df["People"].mean()

peak_crowd = analytics_df["People"].max()

average_dwell = dwell_df["Estimated_Dwell_Time"].mean()

# KPI SECTION
st.markdown("## Operational KPIs")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Crowd",
    round(average_crowd, 2)
)

col2.metric(
    "Peak Occupancy",
    peak_crowd
)

col3.metric(
    "Avg Dwell Time",
    f"{round(average_dwell,2)} sec"
)

# CROWD TREND GRAPH
st.markdown("---")

st.markdown("## Crowd Trend Analysis")

fig1, ax1 = plt.subplots(figsize=(12,5))

fig1.patch.set_facecolor('#0E1117')

ax1.set_facecolor('#1E1E1E')

ax1.plot(
    analytics_df["Frame"],
    analytics_df["People"],
    linewidth=3
)

ax1.set_xlabel("Frame", color='white')

ax1.set_ylabel("People Count", color='white')

ax1.tick_params(colors='white')

for spine in ax1.spines.values():
    spine.set_color('white')

st.pyplot(fig1)

# DWELL TIME GRAPH
st.markdown("---")

st.markdown("## Customer Engagement Duration")

fig2, ax2 = plt.subplots(figsize=(12,5))

fig2.patch.set_facecolor('#0E1117')

ax2.set_facecolor('#1E1E1E')

ax2.bar(
    dwell_df["Person_ID"].astype(str),
    dwell_df["Estimated_Dwell_Time"]
)

ax2.set_xlabel("Customer ID", color='white')

ax2.set_ylabel("Seconds", color='white')

ax2.tick_params(colors='white')

for spine in ax2.spines.values():
    spine.set_color('white')

st.pyplot(fig2)
# HEATMAP SECTION
st.markdown("---")

st.markdown("## Customer Movement Heatmap")

st.image(
    "heatmap.png",
    caption="AI-generated customer activity zones",
    use_container_width=True
)
# BUSINESS INSIGHTS
st.markdown("---")

st.markdown("## AI Business Insights")

st.info(f"""
Peak customer activity reached {peak_crowd} simultaneous visitors.

Average customer occupancy remained at {round(average_crowd,2)} visitors.

Engagement levels indicate moderate-to-high seating interaction.

Potential optimization opportunities exist around peak occupancy periods.
""")

# RAW DATA TABLES
with st.expander("View Raw Analytics Data"):
    st.dataframe(analytics_df)

with st.expander("View Dwell-Time Data"):
    st.dataframe(dwell_df)
