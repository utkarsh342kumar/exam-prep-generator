import streamlit as st
from question_generator import generate_mcqs
from utils import clean_text

# Page setup
st.set_page_config(page_title="Exam Prep Generator", page_icon="✨", layout="wide")

# 🔥 Advanced CSS Styling
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
}

/* Title */
.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    background: -webkit-linear-gradient(#ff9a9e, #fad0c4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
    color: #f1f1f1;
}

/* Glass Card */
.card {
    background: rgba(255, 255, 255, 0.15);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    margin-bottom: 25px;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.02);
}

/* Options */
.option {
    padding: 10px;
    border-radius: 10px;
    margin: 6px 0;
    background: rgba(255,255,255,0.2);
    transition: 0.2s;
}

.option:hover {
    background: rgba(255,255,255,0.4);
}

/* Answer */
.answer {
    color: #00ffcc;
    font-weight: bold;
}

/* Button */
div.stButton > button {
    background: linear-gradient(to right, #ff758c, #ff7eb3);
    color: white;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    border: none;
}

div.stButton > button:hover {
    background: linear-gradient(to right, #43e97b, #38f9d7);
    color: black;
}

/* Input box */
textarea {
    background-color: rgba(255,255,255,0.2) !important;
    color: white !important;
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">✨ Exam Prep Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Create Beautiful MCQs instantly 🚀</div>', unsafe_allow_html=True)

# Input
st.markdown("### 📥 Enter Your Text")
text = st.text_area("", height=200, placeholder="Paste your paragraph here...")

col1, col2 = st.columns(2)

with col1:
    num_q = st.slider("📊 Number of Questions", 3, 10, 5)

with col2:
    difficulty = st.selectbox("🎯 Difficulty Level", ["Auto", "Easy", "Medium", "Hard"])

# Generate Button
if st.button("✨ Generate Questions"):

    if not text.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        text = clean_text(text)
        mcqs = generate_mcqs(text, num_q)

        if not mcqs:
            st.error("No questions generated.")
        else:
            st.success("🎉 Questions Generated!")

            for i, q in enumerate(mcqs):
                st.markdown('<div class="card">', unsafe_allow_html=True)

                st.markdown(f"### 🧠 Q{i+1}. {q['question']}")

                for opt in q["options"]:
                    st.markdown(f'<div class="option">🔹 {opt}</div>', unsafe_allow_html=True)

                st.markdown(f"📊 Difficulty: **{q['difficulty']}**")

                with st.expander("✅ Show Answer"):
                    st.markdown(f'<div class="answer">{q["answer"]}</div>', unsafe_allow_html=True)

                st.markdown('</div>', unsafe_allow_html=True)