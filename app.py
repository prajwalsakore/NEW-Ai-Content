st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
import streamlit as st
from utils import store_user_info

st.set_page_config(page_title="AI Content Genie", layout="wide")

# Apply custom styling
st.markdown("""
    <style>
        .main-title {
            font-size: 3em;
            font-weight: bold;
            color: #FF4B4B;
        }
        .sub-title {
            font-size: 1.5em;
            color: #cccccc;
        }
        .stTextInput > div > div > input {
            background-color: #262730;
            color: white;
        }
        .stSelectbox > div > div {
            background-color: #262730;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main-title">🧠 Welcome to AI Content Genie</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Create engaging blogs, emails, captions — powered by AI!</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🧑‍💻 Enter Your Details")

    name = st.text_input("👤 Enter your full name")
    email = st.text_input("📧 Enter your email")
    role = st.selectbox("💼 What best describes you?", ["Marketer", "Student", "Content Creator", "Business Owner", "Other"])

    if st.button("🚀 Submit"):
        if name and email:
            store_user_info(name, email, role)
            st.success("Your details have been saved!")
        else:
            st.warning("Please enter both your name and email.")
