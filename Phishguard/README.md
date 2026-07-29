# 🛡️ PhishGuard

A machine learning-powered web application that detects whether a URL is **phishing** or **legitimate** — in real time.

## What is PhishGuard?

PhishGuard is a cybersecurity tool that uses machine learning to analyze URLs and determine if they are malicious. Instead of visiting a suspicious link and risking your data, just paste it into PhishGuard and get an instant verdict.

---

## Features

- 🔍 Real-time URL analysis
- 🧠 ML-powered prediction using NLP
- 🎨 Color-coded results (red = phishing, green = legitimate)
- ⚡ Fast and lightweight Flask backend
- 🌐 Clean, simple web interface

---

## How It Works

1. User pastes a URL into the web form
2. The URL is cleaned — strips `http://`, `https://`, `www.`
3. Cleaned URL is vectorized using a pre-trained **CountVectorizer**
4. Feature vector is passed to the trained **ML model**
5. Result is displayed:
   - 🔴 `This is a Phishing Website !!`
   - 🟢 `This is a Legitimate Website !!`

---

## Machine Learning

### Dataset
- [Phishing Site URLs — Kaggle](https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls)
- Hundreds of thousands of labeled URLs (`good` / `bad`)

### Models Evaluated
| Model | Description |
|---|---|
| Logistic Regression | Linear classifier, fast and interpretable |
| Naive Bayes (Multinomial) | Probabilistic, great for text data |
| Random Forest | Ensemble of decision trees, high accuracy |
| Support Vector Machine | Finds optimal decision boundary |

The best performing model is saved as `model.pkl` and used for live predictions.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Web Framework | Flask |
| ML Library | scikit-learn |
| NLP | CountVectorizer |
| Data Processing | Pandas, NumPy |
| Frontend | HTML, CSS (Jinja2) |

---

## Project Structure

```
PhishGuard/
├── app.py                  # Flask application
├── templates/
│   └── index.html          # Frontend UI
├── model.pkl               # Trained ML model
├── mnb.pkl                 # Naive Bayes model
├── vectorizer.pkl          # Trained CountVectorizer
├── requirements.txt        # Dependencies
└── README.md
```

---

## Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/your-username/PhishGuard.git
cd PhishGuard

# 2. Create virtual environment
python -m venv env
env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## Usage

| Input URL | Result |
|---|---|
| `yeniik.com.tr/wp-admin/js/login.alibaba.com/login.jsp.php` | 🔴 Phishing |
| `www.youtube.com/` | 🟢 Legitimate |
| `https://www.google.com` | 🟢 Legitimate |

---

## Dependencies

```
flask==3.0.3
scikit-learn==1.4.2
pandas==2.2.2
numpy==1.26.4
nltk==3.8.1
```

---

## License

Built for educational purposes. Not intended for production use.
