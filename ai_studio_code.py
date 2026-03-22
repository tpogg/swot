import streamlit as st
import pandas as pd
import plotly.express as px
from textblob import TextBlob
import json

# --- UI CONFIGURATION ---
st.set_page_config(page_title="User Intelligence Suite", layout="wide")

# Custom CSS for a "Dark Mode" Cyberpunk feel
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .swot-box {
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 10px;
        height: 300px;
        overflow-y: auto;
        border: 1px solid #333;
    }
    .strength { background-color: #1b4332; border-left: 5px solid #2d6a4f; }
    .weakness { background-color: #432818; border-left: 5px solid #99582a; }
    .opportunity { background-color: #183a43; border-left: 5px solid #2a6f97; }
    .threat { background-color: #431818; border-left: 5px solid #9a031e; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ Recon Suite")
    api_key = st.text_input("OpenAI API Key", type="password")
    target_user = st.text_input("Target Username", placeholder="e.g. CyberNinja99")
    st.divider()
    st.info("Upload logs from Discord, Reddit, or X to begin analysis.")

# --- MAIN INTERFACE ---
st.title(f"Identity Analysis: {target_user if target_user else 'No User Selected'}")

tab1, tab2, tab3 = st.tabs(["📂 Data Ingestion", "📊 SWOT Dashboard", "📈 Behavioral Trends"])

with tab1:
    st.subheader("Upload Platform Archives")
    col1, col2 = st.columns(2)
    with col1:
        uploaded_files = st.file_uploader("Drop JSON/CSV/JS files here", accept_multiple_files=True)
    with col2:
        st.write("🔍 **Supported Platforms:**")
        st.caption("- Discord (messages.json)")
        st.caption("- Reddit (comments.csv)")
        st.caption("- X/Twitter (tweets.js)")

with tab2:
    if not uploaded_files:
        st.warning("Please upload data in the first tab to generate the SWOT grid.")
    else:
        # Mocking the AI response structure for the UI preview
        # In the real app, this text comes from the OpenAI function
        col_top_1, col_top_2 = st.columns(2)
        
        with col_top_1:
            st.markdown('<div class="swot-box strength"><h3>✅ Strengths</h3>'
                        '<ul><li>High technical proficiency in Python</li>'
                        '<li>Consistent helpfulness in community logs</li>'
                        '<li>Strong leadership traits in Discord</li></ul></div>', unsafe_allow_html=True)
        
        with col_top_2:
            st.markdown('<div class="swot-box weakness"><h3>⚠️ Weaknesses</h3>'
                        '<ul><li>Occasional aggressive tone in debates</li>'
                        '<li>Frequent late-night posting (Fatigue signs)</li>'
                        '<li>Repetitive use of informal slang</li></ul></div>', unsafe_allow_html=True)

        col_bot_1, col_bot_2 = st.columns(2)
        
        with col_bot_1:
            st.markdown('<div class="swot-box opportunity"><h3>🚀 Opportunities</h3>'
                        '<ul><li>Mentioned interest in AI Security</li>'
                        '<li>Strong network with industry influencers</li>'
                        '<li>Potential for Moderator roles</li></ul></div>', unsafe_allow_html=True)
        
        with col_bot_2:
            st.markdown('<div class="swot-box threat"><h3>🚨 Threats</h3>'
                        '<ul><li>Username found in 2 data breaches</li>'
                        '<li>Location details leaked in Reddit posts</li>'
                        '<li>Pattern matches a known public identity</li></ul></div>', unsafe_allow_html=True)

with tab3:
    st.subheader("Sentiment Analysis Over Content")
    
    # Example Chart Generation
    chart_data = pd.DataFrame({
        'Post Number': range(1, 21),
        'Sentiment Score': [0.1, 0.4, -0.2, 0.5, 0.8, -0.1, 0.3, 0.2, -0.5, 0.1, 0.4, 0.6, 0.2, -0.1, 0.1, 0.5, 0.9, 0.2, -0.2, 0.3]
    })
    
    fig = px.area(chart_data, x='Post Number', y='Sentiment Score', 
                  title="Positivity vs. Negativity Trend",
                  color_discrete_sequence=['#00d4ff'])
    st.plotly_chart(fig, use_container_width=True)

    col_stats1, col_stats2, col_stats3 = st.columns(3)
    col_stats1.metric("Post Volatility", "Medium", "-5%")
    col_stats2.metric("Dominant Emotion", "Analytical", "+12%")
    col_stats3.metric("Privacy Risk", "High", "Critical", delta_color="inverse")