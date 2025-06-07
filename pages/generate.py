
import streamlit as st

st.set_page_config(
    page_title="AI Content Genie",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
        padding: 2rem;
    }
    .block-container {
        padding: 2rem 1rem 2rem 1rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        font-size: 1.1em;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>input {
        border-radius: 10px;
        padding: 10px;
        font-size: 1em;
    }
    .stSelectbox>div>div {
        border-radius: 10px;
        padding: 10px;
        font-size: 1em;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #2c3e50;
    }
    .css-1d391kg {
        background-color: #ffffff !important;
        border-right: 2px solid #f1f1f1;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712100.png", width=80)
    st.markdown("## 🧠 AI Content Genie")
    st.markdown("### Navigation:")
    st.markdown("""
- 🏠 Home  
- ✍️ Generate  
- 💡 Content Ideas  
- 📊 User Info  
- 🧾 Plans and Billing  
- 🤖 Chatbot
    """)
    st.markdown("---")
    st.caption("🚀 Built with Streamlit + OpenAI")

st.title("✍️ Generate Content")

option = st.selectbox("What do you want to generate?", ["Blog", "Email", "Caption"])

prompt = st.text_area("Enter a brief topic or idea:")

if st.button("🚀 Generate"):
    st.success(f"Generated {option.lower()} for: {prompt}")
