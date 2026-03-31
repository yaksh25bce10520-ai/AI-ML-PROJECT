# AI-ML-PROJECT
The AI Chatbot with Machine Learning and Utilities is a Python-based command-line application designed to simulate intelligent conversation while also providing useful built-in features such as calculations and data visualization. The primary purpose of this project was to develop a functional chatbot from scratch using Natural Language Processing (NLP) and basic Machine Learning techniques, without relying on advanced frameworks. By leveraging libraries like NLTK for text processing, Scikit-learn for model training, and Matplotlib for visualization, the project demonstrates how different components of Python can be integrated to create a smart and interactive system. The chatbot is trained using a dataset of predefined intents stored in a JSON file, where each intent includes patterns and corresponding responses. User input is processed through tokenization and stemming, converted into a bag-of-words representation, and then passed into a Logistic Regression model to predict the most relevant intent. Based on this prediction, the chatbot generates an appropriate response, and if the confidence level is low, it gracefully handles the situation by asking the user to rephrase the input. In addition to conversational abilities, the chatbot includes a memory feature that allows it to store and recall user-specific information, such as remembering a user's name. It also functions as a basic calculator capable of solving arithmetic expressions entered by the user. Furthermore, it provides data visualization utilities, enabling users to generate pie charts and bar graphs by inputting labels and values interactively. To run the application, users must install required libraries such as nltk, scikit-learn, matplotlib, and numpy, and download necessary NLTK datasets. Once executed, the chatbot operates in a continuous loop, accepting user input until the user chooses to exit. Overall, this project serves as a practical demonstration of combining machine learning, NLP, and user interaction within a single application, making it both a learning tool and a useful utility-driven chatbot.
Got it — you want a **professional GitHub-style README (repo description)** just like your Image-to-PDF one, but for your **AI Chatbot with ML + Utilities project**.

Here’s a clean, ready-to-use version 👇

---

# 🤖 AI Chatbot with Machine Learning + Utilities (Python)

A smart, command-line based AI chatbot built using Python and basic Machine Learning techniques. This chatbot not only handles conversational queries but also includes utility features like calculations, memory handling, and data visualization (charts).

---

## ⚙️ Purpose

### 🎯 Purpose Behind the Project:

The goal of this project was to build an **intelligent chatbot from scratch** using Natural Language Processing (NLP) and Machine Learning concepts without relying on heavy frameworks.

Unlike simple rule-based bots, this chatbot:

* Learns intent patterns using **Logistic Regression**
* Processes text using **NLTK**
* Provides **interactive utilities** like charts and calculations

---

### 💡 Learning Outcomes:

This project helped in understanding:

* NLP basics (tokenization, stemming, stopword removal)
* Building a **Bag of Words model**
* Training ML models using **Scikit-learn**
* Designing an **interactive CLI chatbot**
* Handling real-time user input and dynamic responses
* Integrating **data visualization (Matplotlib)**

---

## 📊 Key Features & Data Handling

### 🚀 Key Features:

* 💬 **Conversational Chatbot**

  * Responds to greetings, help, thanks, etc.

* 🧠 **Machine Learning-Based Intent Recognition**

  * Uses Logistic Regression to classify user input

* 🧾 **Memory Feature**

  * Stores user name and recalls it later

* 🧮 **Built-in Calculator**

  * Solves expressions like `2 + 3 * 4`

* 📊 **Data Visualization**

  * Generate:

    * Pie Charts
    * Bar Graphs

* ⚡ **Fallback Handling**

  * Responds when input is not understood

---

### 📁 Data Description:

| Variable / Type | Description                                       |
| --------------- | ------------------------------------------------- |
| `intent.json`   | Contains chatbot intents, patterns, and responses |
| `words`         | Processed vocabulary (stemmed words)              |
| `labels`        | Intent categories                                 |
| `training`      | Bag-of-words training data                        |
| `output`        | Expected outputs for training                     |
| `memory`        | Dictionary storing user-specific data             |
| `model`         | Trained Logistic Regression model                 |

---

## 🧠 How It Works

1. User input is tokenized using **NLTK**
2. Words are stemmed and converted into a **bag-of-words vector**
3. The trained ML model predicts the **intent**
4. The bot selects a response based on probability
5. If confidence is low → fallback message

---

## 🚀 How to Use

### 🔧 Prerequisites

Make sure you have Python 3.x installed.

Install required libraries:

```bash
pip install nltk scikit-learn matplotlib numpy
```

Also download NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

### ▶️ Run the Application

```bash
python main.py
```

---

### 💻 Application Instructions

* Type normal messages → chatbot replies
* Type `help` → shows features
* Type `quit` → exit chatbot

#### Special Commands:

* 🧠 `my name is Yaksh` → stores your name
* ❓ `what is my name` → recalls your name
* 🧮 `5 + 6 * 2` → calculator
* 📊 `pie` → create pie chart
* 📊 `bar` → create bar graph

---

## 📞 Contact Information

* Name: Yaksh Malasiya
* Email: yaksh.25bce10520@vitbhopal.ac.in
* GitHub: ()

---

## 📄 License

This project is released under the **MIT License**.
You are free to use, modify, and distribute it with proper attribution.

---

 Future Improvements

* GUI version using Tkinter
* Deep Learning model (LSTM / Transformers)
* Voice assistant integration
* Web deployment (Flask / Streamlit)



