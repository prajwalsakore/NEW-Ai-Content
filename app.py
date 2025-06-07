import streamlit as st

st.set_page_config(
    page_title="AI Content Genie",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS styles
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

# Sidebar content
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712100.png", width=80)
    st.markdown("## 🧠 AI Content Genie")
    page = st.radio("Navigation", ["Home", "Generate", "Content Ideas", "User Info", "Plans and Billing", "Chatbot"])
    st.markdown("---")
    st.caption("🚀 Built with Streamlit + OpenAI")

# Main content based on navigation
if page == "Home":
    st.title("🧠 Welcome to AI Content Genie")
    st.markdown("Use the sidebar to navigate through the app.")

elif page == "Generate":
    st.title("✍️ Generate Content")
    st.markdown("Here you can generate blogs, emails, and other content.")

elif page == "Content Ideas":
    st.title("💡 Content Ideas")
    st.markdown("Get fresh ideas for your content creation.")

elif page == "User Info":
    st.title("📊 User Info")
    st.markdown("View and manage your user details here.")

elif page == "Plans and Billing":
    st.title("🧾 Plans and Billing")
    st.markdown("Manage your subscription plans and billing information here.")

elif page == "Chatbot":
    st.title("🤖 Chatbot")
    st.markdown("Chat with the AI-powered assistant.")


