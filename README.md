# 💜 AI Sentiment-Based Text Generator

**Remote ML Internship Project | AI Text Generation based on Sentiment**

This project is a **Streamlit-based AI web application** that generates paragraphs or essays based on the sentiment of a user’s prompt. It detects the sentiment (Positive, Negative, Neutral) automatically or allows manual selection, then generates coherent text aligned with that sentiment.

---

## 🎯 Objective

The goal of this project is to demonstrate an AI system that:

- Understands the sentiment of an input prompt.
- Produces text aligned with the detected or selected sentiment.
- Provides an interactive and user-friendly interface for users to experiment with AI-generated content.

This project was developed as part of a **Remote ML Internship Task Assessment**.

---
## 🚀 Live Demo

Try the app online here: [AI Sentiment-Based Text Generator](https://ai-sentiment-text-generator-3u4rbaggwbembzy9aug7oo.streamlit.app/)

---
## 🛠️ Features

- **Sentiment Analysis:** Automatically detect the sentiment of your input text.
- **Manual Sentiment Selection:** Choose Positive, Negative, or Neutral manually if preferred.
- **Text Generation:** Generates coherent and sentiment-aligned paragraphs using GPT-2.
- **Adjustable Output Length:** Short, Medium, or Long text generation options.
- **Modern Lavender UI:** Light purple and white theme with rounded input/output boxes.
- **Interactive Frontend:** Developed using Streamlit for instant feedback.

---

## 📂 Project Structure

AI-Sentiment-Text-Generator/
│
├─ app.py # Main Streamlit app
├─ requirements.txt # Python dependencies
├─ README.md # Project documentation
└─ .gitignore # Optional, for ignoring unnecessary files
---

## ⚡ Installation

1. Clone this repository:

```bash
git clone https://github.com/vedant7115/AI-Sentiment-Text-Generator.git
cd AI-Sentiment-Text-Generator
pip install -r requirements.txt

```

## 🧠 Technical Approach

### Sentiment Analysis
- Uses `distilbert-base-uncased-finetuned-sst-2-english` from Hugging Face Transformers.
- Detects whether input text is **Positive**, **Negative**, or **Neutral**.

### Text Generation
- GPT-2 model generates text aligned with the detected sentiment.
- Output length and style controlled via adjustable parameters.

### Frontend
- Built with Streamlit.
- Lavender-white theme with modern input/output cards.
- Sidebar allows sentiment selection and output length adjustments.

---

## ⚡ Usage

1. Enter a prompt in the input box.
2. Select **Auto Detect** or choose a sentiment manually.
3. Choose output length (**Short**, **Medium**, **Long**).
4. Click **Generate Text** to see AI-generated output in a styled card.

---

## 📈 Project Challenges

- Ensuring text generation aligns with the detected sentiment.
- Managing output length without cutting off sentences awkwardly.
- Designing a clean, interactive, and
---

## 💾 Future Improvements

- Add download option for generated text.
- Include multiple language support.
- Add custom GPT-2 fine-tuning for more context-aware outputs.
- Deploy on Streamlit Cloud or Heroku for public access.

---

## 📌 Notes

- This project was completed under a **Remote ML Internship Task Assessment** with the objective of building an AI-based text generator aligned with sentiment.
- All models used are **pre-trained Hugging Face Transformers**.
- No personal or sensitive data is required to run this application.

---

## 📌 References

- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers/index)
- [Streamlit Documentation](https://docs.streamlit.io/)
- GPT-2 model: [OpenAI GPT-2](https://huggingface.co/gpt2)

---

## 👨‍💻 Author

**Vedant Saubhri – Machine Learning Enthusiast & Developer**  
Email: singhvedant7115@gmail.com
