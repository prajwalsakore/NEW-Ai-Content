import streamlit as st

st.set_page_config(
    page_title="AI Content Genie",
    page_icon="🧠",
    layout="wide"
)

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Rest of your app code below...


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

# Sidebar navigation
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712100.png", width=80)
    st.markdown("## 🧠 AI Content Genie")
    page = st.radio("Navigation", [
        "Home",
        "Generate",
        "Content Ideas",
        "User Info",
        "Plans and Billing",
        "Chatbot"
    ])
    st.markdown("---")
    st.caption("🚀 Built with Streamlit + OpenAI")

# --- Page content ---

if page == "Home":
    st.title("🧠 Welcome to AI Content Genie")
    st.markdown("""
    Welcome to AI Content Genie, your AI-powered assistant to generate blogs, emails, content ideas, and more.
    
    Use the sidebar to explore different features.
    """)

elif page == "Generate":
    st.title("✍️ Generate Content")
    st.markdown("Create blog posts, marketing emails, social media captions, and other content here.")
    
    prompt = st.text_area("Enter your content prompt")
    if st.button("Generate"):
        if prompt.strip() == "":
            st.warning("Please enter a prompt to generate content.")
        else:
            st.info(f"Generating content for prompt: {prompt}")
            # Call your AI generation logic here and display results
            st.success("Content generated successfully! (Demo placeholder)")

elif page == "Content Ideas":
    st.title("💡 Content Ideas")
    st.markdown("""
    Discover fresh and trending content ideas based on your niche or interests.
    """)
    niche = st.text_input("Enter your niche or topic")
    if st.button("Get Ideas"):
        if niche.strip() == "":
            st.warning("Please enter a niche or topic.")
        else:
            st.info(f"Fetching content ideas for: {niche}")
            # Integrate AI or database call here
            st.success("Here are some content ideas! (Demo placeholder)")

elif page == "User Info":
    st.title("📊 User Info")
    st.markdown("Provide your details to personalize your experience.")

    username = st.text_input("Username")
    full_name = st.text_input("Full Name")
    email = st.text_input("Email ID")
    role = st.selectbox("Role", ["Marketer", "Student", "Content Creator", "Other"])

    if st.button("Submit"):
        if not username or not full_name or not email:
            st.error("Please fill in all fields.")
        else:
            st.success(f"Thanks {full_name}! Your info has been saved.")
            # Save or process user info here

elif page == "Plans and Billing":
    st.title("🧾 Plans and Billing")
    st.markdown("""
    Manage your subscription plans and billing here.

    **Available Plans:**

    - **Basic** - ₹299/month
    - **Pro** - ₹599/month
    - **Premium** - ₹999/month
    """)

    selected_plan = st.radio("Select a plan", ["Basic", "Pro", "Premium"])
    st.markdown(f"### You selected: {selected_plan}")

    st.subheader("Make a Payment")
    amount = st.number_input("Enter amount (₹)", min_value=0, value=299 if selected_plan=="Basic" else 599 if selected_plan=="Pro" else 999)
    payment_method = st.selectbox("Select Payment Gateway", ["PhonePe", "Razorpay"])
    card_number = st.text_input("Card Number", max_chars=16, help="Enter 16-digit card number")
    cvv = st.text_input("CVV", max_chars=3, type="password", help="Enter 3-digit CVV")

    if st.button("Pay Now"):
        if amount <= 0:
            st.error("Please enter a valid amount.")
        elif len(card_number) != 16 or not card_number.isdigit():
            st.error("Please enter a valid 16-digit card number.")
        elif len(cvv) != 3 or not cvv.isdigit():
            st.error("Please enter a valid 3-digit CVV.")
        else:
            # Dummy success message - Replace with real payment integration later
            st.success(f"Payment of ₹{amount} via {payment_method} successful! 🎉")

elif page == "Chatbot":
    st.title("🤖 Chatbot")
    st.markdown("Chat with the AI-powered assistant.")

    user_input = st.text_input("Ask me anything...")
    if st.button("Send"):
        if user_input.strip() == "":
            st.warning("Please enter a message.")
        else:
            st.info(f"Chatbot reply to: {user_input}")
            # Integrate your chatbot backend here
            st.success("Here is the chatbot response! (Demo placeholder)")



