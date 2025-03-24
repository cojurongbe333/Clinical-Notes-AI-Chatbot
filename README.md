
# 🧠 MedAssistAI — NLP Clinical Note Summarizer + QA Chatbot

MedAssistAI is an NLP-powered Streamlit app that summarizes clinical notes and answers medical questions using state-of-the-art transformer models.

---

## 🚀 Features
- Summarizes long clinical notes using `facebook/bart-large-cnn`
- Answers follow-up clinical questions using `distilbert-base-cased-distilled-squad`
- Streamlit frontend for usability
- Power BI dashboard for usage insights

---

## 🛠️ How to Run

### Locally (with Docker):
```bash
docker build -t medassistai .
docker run -p 8501:8501 medassistai
```

### Or using Streamlit:
```bash
pip install -r requirements.txt
streamlit run streamlit_medassistai.py
```

---

## 🧪 Sample Question
```json
{
  "note": "Patient is recovering well from cardiac surgery...",
  "question": "What is the treatment plan?"
}
```

---

## 📊 Power BI
Includes mock `summary_log.csv` for dashboarding:
- Summary length trends
- Usage by department
- QA response times

---

## 📁 File Structure
```
├── data/                       # Synthetic clinical notes
├── notebooks/                 # EDA, Summarization & QA
├── streamlit_medassistai.py   # App frontend
├── summary_log.csv            # For Power BI
├── requirements.txt
├── Dockerfile
└── README.md
```
