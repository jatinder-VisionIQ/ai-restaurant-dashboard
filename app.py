import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from ultralytics import YOLO
import cv2
import tempfile

# PAGE CONFIG
st.set_page_config(
    page_title="VisionIQ Analytics",
    layout="wide"
)

# DARK THEME
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

# VIDEO UPLOADER
uploaded_file = st.file_uploader(
    "Upload Restaurant Video",
    type=["mp4", "mov", "avi"]
)

# PROCESS VIDEO
if uploaded_file is not None:

    st.success("Video uploaded successfully!")

    # SAVE TEMP VIDEO
    temp_file = tempfile.NamedTemporaryFile(delete=False)

    temp_file.write(uploaded_file.read())

    video_path = temp_file.name

    # LOAD YOLO MODEL
    model = YOLO("yolov8n.pt")

    # READ VIDEO
    video = cv2.VideoCapture(video_path)

    frame_count = 0

    analytics_data = []

    # ANALYZE VIDEO
    with st.spinner("AI is analyzing customer behavior..."):

        while True:

            success, frame = video.read()

            if not success:
                break

            frame_count += 1

            # Analyze every 30th frame
            if frame_count % 30 == 0:

                results = model(frame)

                person_count = 0

                for result in results:

                    boxes = result.boxes

                    for box in boxes:

                        class_id = int(box.cls[0])

                        # Person class
                        if class_id == 0:
                            person_count += 1

                analytics_data.append({
                    "Frame": frame_count,
                    "People": person_count
                })

    # CREATE DATAFRAME
    analytics_df = pd.DataFrame(analytics_data)

    # KPI CALCULATIONS
    average_crowd = analytics_df["People"].mean()
    peak_crowd = analytics_df["People"].max()

    # KPI SECTION
    st.markdown("## Operational KPIs")

    col1, col2 = st.columns(2)

    col1.metric(
        "Average Crowd",
        round(average_crowd,2)
    )

    col2.metric(
        "Peak Occupancy",
        peak_crowd
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

    # BUSINESS INSIGHTS
    st.markdown("---")

    st.markdown("## AI Business Insights")

    st.info(f"""
    Peak customer activity reached {peak_crowd} simultaneous visitors.

    Average customer occupancy remained at {round(average_crowd,2)} visitors.

    Crowd movement patterns indicate active engagement periods.
    """)

    # RAW DATA
    with st.expander("View Analytics Data"):
        st.dataframe(analytics_df)
