import streamlit as st
from transformers import pipeline

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="AI Sentiment Text Generator",
    page_icon="💜",
    layout="centered",
)

# -------------------- CUSTOM STYLES --------------------
st.markdown("""
    <style>
    body {
        background-color: #E6E6FA; /* Soft lavender background */
    }
    .main {
        background-color: #E6E6FA;
        color: #2E2E2E;
        font-family: 'Poppins', sans-serif;
        padding-top: 2rem;
    }
    .app-card {
        background-color: #FFFFFF;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0px 4px 20px rgba(181, 126, 220, 0.2);
        max-width: 800px;
        margin: auto;
    }
    h1, h2, h3, h4 {
        color: #7B68EE; /* Medium lavender text */
    }
    .stTextArea textarea {
        border-radius: 15px;
        border: 2px solid #B57EDC;
        background-color: #FFFFFF;
        color: #2E2E2E;
        font-size: 16px;
    }
    .stButton button {
        background-color: #B57EDC;
        color: white;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
        border: none;
        transition: 0.2s ease;
    }
    .stButton button:hover {
        background-color: #9B59B6;
        color: white;
        transform: scale(1.05);
    }
    .output-box {
        background-color: #FFFFFF;
        padding: 1.2rem;
        border-radius: 12px;
        border: 1.5px solid #B57EDC;
        margin-top: 1.5rem;
        font-size: 16px;
        line-height: 1.6;
        color: #2E2E2E;
    }
    .sidebar .sidebar-content {
        background-color: #F3E8FF;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- LOAD MODELS --------------------
@st.cache_resource
def load_pipelines():
    # Explicit model names for reliability
    sentiment_analyzer = pipeline(
        "sentiment-analysis",
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )
    text_generator = pipeline("text-generation", model="gpt2")
    return sentiment_analyzer, text_generator

sentiment_analyzer, text_generator = load_pipelines()

# -------------------- SIDEBAR --------------------
st.sidebar.title("⚙️ Model Controls")
st.sidebar.markdown("Customize how the AI behaves.")

mode = st.sidebar.selectbox("Sentiment Mode", ["Auto Detect", "Positive", "Negative", "Neutral"])
length = st.sidebar.radio("Output Length", ["Short", "Medium", "Long"])
length_mapping = {"Short": 50, "Medium": 100, "Long": 200}

st.sidebar.markdown("---")
st.sidebar.markdown("💡 *Tip:* Use 'Auto Detect' to let AI infer mood from your text.")

# -------------------- MAIN INTERFACE --------------------
st.markdown("<div class='app-card'>", unsafe_allow_html=True)
st.title("💜 AI Sentiment-Based Text Generator")
st.subheader("Generate meaningful paragraphs that match your mood 🌸")

prompt = st.text_area(
    "Enter your prompt below:",
    height=150,
    placeholder="Type something like 'I’m feeling great about my progress today!'"
)

if st.button("✨ Generate Text"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt before generating.")
    else:
        with st.spinner("Analyzing sentiment and generating text..."):
            # Detect or use manual sentiment
            if mode == "Auto Detect":
                sentiment = sentiment_analyzer(prompt)[0]['label']
            else:
                sentiment = mode

            st.write(f"**Detected/Selected Sentiment:** `{sentiment}`")

            # Sentiment-aligned generation
            sentiment_prefix = {
                "POSITIVE": "A cheerful and uplifting paragraph:",
                "NEGATIVE": "A serious or somber paragraph:",
                "NEUTRAL": "A balanced and factual paragraph:",
                "Positive": "A cheerful and uplifting paragraph:",
                "Negative": "A serious or somber paragraph:",
                "Neutral": "A balanced and factual paragraph:"
            }

            input_text = f"{sentiment_prefix.get(sentiment, '')} {prompt}"
            generated = text_generator(
                input_text,
                max_length=length_mapping[length],
                num_return_sequences=1,
                temperature=0.8,  # smoother outputs
                top_p=0.9,
                do_sample=True
            )[0]['generated_text']

        st.markdown("<div class='output-box'><strong>📝 Generated Text:</strong><br><br>" +
                    generated + "</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
