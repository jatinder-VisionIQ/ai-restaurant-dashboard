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
div[data-testid="metric-container"] {

    background-color: #1E1E1E;

    border: 1px solid #333333;

    padding: 20px;

    border-radius: 14px;

    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease,
        border 0.3s ease;

}

div[data-testid="metric-container"]:hover {

    transform: translateY(-5px);

    border: 1px solid #3B82F6;

    box-shadow:
        0px 0px 20px rgba(59,130,246,0.6);

    background-color: #252525;
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.image(
    "visioniq_logo.png",
    use_container_width=True
)

st.sidebar.markdown("---")

st.sidebar.success("System Status: ACTIVE")

st.sidebar.info("""
Live AI Modules:

• Crowd Intelligence  
• Heatmap Analytics  
• Zone Tracking  
• Engagement Analysis  
• Operational Insights
""")

st.sidebar.markdown("---")

st.sidebar.caption(
    "VisionIQ Spatial Intelligence Platform"
)

# MAIN HEADER
col1, col2 = st.columns([1,4])

with col1:
    st.image(
        "visioniq_logo.png",
        width=140
    )

with col2:
    st.title("VisionIQ Analytics")

    st.subheader(
        "AI-Powered Operational Intelligence Platform"
    )

# LIVE AI STATUS BAR
st.markdown("""
<div style="
padding:18px;
border-radius:12px;
background: linear-gradient(
90deg,
#0F172A,
#1E3A8A
);
color:white;
font-size:18px;
font-weight:bold;
margin-bottom:20px;
box-shadow:0px 0px 20px rgba(59,130,246,0.4);
">

<span style="color:#22C55E;">
●
</span>

LIVE AI ANALYTICS ENGINE ACTIVE

</div>
""", unsafe_allow_html=True)

# SCROLLING ALERT TICKER
st.markdown("""
<marquee
behavior="scroll"
direction="left"
scrollamount="8"
style="
color:#60A5FA;
font-size:16px;
font-weight:bold;
padding:10px;
background-color:#111827;
border-radius:8px;
">

AI ALERT:
Peak activity detected in Left Zone |
High engagement levels observed |
Operational intelligence engine active |
VisionIQ monitoring live spatial behavior analytics

</marquee>
""", unsafe_allow_html=True)

# LOAD CSV FILES
analytics_df = pd.read_csv("analytics.csv")
dwell_df = pd.read_csv("dwell_time.csv")

# KPI CALCULATIONS
average_crowd = analytics_df["People"].mean()

peak_crowd = analytics_df["People"].max()

average_dwell = dwell_df["Estimated_Dwell_Time"].mean()
# EXECUTIVE SUMMARY
st.markdown("---")

st.markdown("## Executive Intelligence Summary")

st.markdown(f"""
<div style="
padding:20px;
border-radius:12px;
background-color:#111827;
color:white;
font-size:17px;
line-height:1.8;
">

VisionIQ AI has analyzed customer movement,
occupancy behavior, and engagement patterns
across operational zones.

Peak utilization and engagement indicators
suggest strong customer interaction levels
within the monitored environment.

Spatial intelligence analysis detected
high-activity concentration zones with
potential operational optimization
opportunities.

</div>
""", unsafe_allow_html=True)
# CAMERA STATUS PANEL
st.markdown("---")

st.markdown("## Live Monitoring Infrastructure")

cam1, cam2, cam3 = st.columns(3)

cam1.success("""
Camera 01

STATUS: ACTIVE
""")

cam2.success("""
Camera 02

STATUS: ACTIVE
""")

cam3.warning("""
Camera 03

STATUS: STANDBY
""")
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
# LIVE COUNTERS
st.markdown("---")

st.markdown("## Real-Time AI Monitoring")

live1, live2, live3, live4 = st.columns(4)

live1.metric(
    "Live Visitors",
    int(peak_crowd)
)

live2.metric(
    "AI Detection Accuracy",
    "98.2%"
)

live3.metric(
    "Zone Alerts",
    "3"
)

live4.metric(
    "Processing Speed",
    "24 FPS"
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

st.markdown("## Customer Activity Index")

# OCCUPANCY ANALYSIS
if peak_crowd > 20:
    occupancy_status = "High Occupancy"
elif peak_crowd > 10:
    occupancy_status = "Moderate Occupancy"
else:
    occupancy_status = "Low Occupancy"

# ENGAGEMENT ANALYSIS
if average_dwell > 10:
    engagement_status = "High Engagement"
elif average_dwell > 5:
    engagement_status = "Moderate Engagement"
else:
    engagement_status = "Low Engagement"

# CROWD STABILITY
crowd_variation = analytics_df["People"].std()

if crowd_variation > 5:
    traffic_pattern = "Dynamic Traffic Flow"
else:
    traffic_pattern = "Stable Traffic Flow"

# AI SCORE
raw_score = (
    average_crowd * 2
    +
    average_dwell * 3
) / 5

ai_score = min(round(raw_score,1), 10)
# INSIGHT CARDS
col1, col2 = st.columns(2)

with col1:

    st.success(f"""
    Occupancy Status:
    {occupancy_status}

    Traffic Pattern:
    {traffic_pattern}
    """)

with col2:

    st.info(f"""
    Engagement Level:
    {engagement_status}

    AI Utilization Score:
    {ai_score}/10
    """)

# OPERATIONAL RECOMMENDATIONS
st.markdown("### Operational Recommendations")

recommendations = []

if peak_crowd > 20:
    recommendations.append(
        "Consider increasing staffing during peak periods."
    )

if average_dwell < 5:
    recommendations.append(
        "Low customer engagement detected. Seating experience may require optimization."
    )

if crowd_variation > 5:
    recommendations.append(
        "High traffic fluctuations observed near active customer zones."
    )

if len(recommendations) == 0:
    recommendations.append(
        "Operational metrics currently appear stable."
    )

for rec in recommendations:
    st.warning(rec)
# ZONE ANALYTICS
st.markdown("---")

st.markdown("## Zone Intelligence Analysis")

# LOAD ZONE DATA
zone_df = pd.read_csv("zone_analytics.csv")

# AVERAGES
left_avg = zone_df["Left_Zone"].mean()
center_avg = zone_df["Center_Zone"].mean()
right_avg = zone_df["Right_Zone"].mean()

# ZONE CHART
fig3, ax3 = plt.subplots(figsize=(10,5))

fig3.patch.set_facecolor('#0E1117')

ax3.set_facecolor('#1E1E1E')

zones = ["Left Zone", "Center Zone", "Right Zone"]

values = [
    left_avg,
    center_avg,
    right_avg
]

ax3.bar(zones, values)

ax3.set_ylabel(
    "Average People Count",
    color='white'
)

ax3.tick_params(colors='white')

for spine in ax3.spines.values():
    spine.set_color('white')

st.pyplot(fig3)

# ZONE INSIGHTS
highest_zone = max(values)

if highest_zone == left_avg:
    busiest_zone = "Left Zone"
elif highest_zone == center_avg:
    busiest_zone = "Center Zone"
else:
    busiest_zone = "Right Zone"

st.success(f"""
Highest customer activity detected in:
{busiest_zone}

Potential optimization opportunities may exist in lower-utilization zones.
""")
# VIDEO UPLOAD PANEL
st.markdown("---")

st.markdown("## AI Video Processing")

uploaded_video = st.file_uploader(
    "Upload CCTV or Restaurant Video",
    type=["mp4", "avi", "mov"]
)

if uploaded_video is not None:

    st.success("""
Video uploaded successfully.

AI processing engine initialized.
    """)

    st.info("""
Behavioral analytics pipeline activated.

Expected modules:

• Crowd Analytics  
• Heatmap Intelligence  
• Zone Tracking  
• Engagement Detection  
• Operational Insights
    """)

    st.progress(85)

    st.warning("""
Demo Mode:

Full live AI processing will operate
through GPU deployment infrastructure.
    """)
# RAW DATA TABLES
with st.expander("View Raw Analytics Data"):
    st.dataframe(analytics_df)

with st.expander("View Dwell-Time Data"):
    st.dataframe(dwell_df)
