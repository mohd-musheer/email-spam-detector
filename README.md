# 📧 Email Spam Detector

A simple and effective **Machine Learning–based Email Spam Detection system** that classifies emails as **Spam** or **Not Spam** using Natural Language Processing (NLP) with 98.55 % Accuracy

🚀 **Live Demo:**  
👉 https://email-spam-detector-3gon.onrender.com

📦 **Docker Image :**  
👉 https://hub.docker.com/repository/docker/mohdmusheer/email-spam-detector

---

## 🧠 Project Overview

Email spam is a common problem that affects productivity and security.  
This project uses **Machine Learning + NLP** to automatically detect whether an email message is spam or legitimate.

The model is trained on a labeled dataset of emails and deployed as a **web application** where users can simply enter an email message and instantly get the result.

---

## ✨ Features

- ✅ Classifies emails as **Spam** or **Not Spam**
- ✅ User-friendly web interface
- ✅ End-to-end ML pipeline
- ✅ Real-time predictions
- ✅ Deployed online (Render)
- ✅ Clean & simple code structure

---

## 🛠️ Tech Stack

### 🔹 Machine Learning
- Logistic Regression / Naive Bayes  
- TF-IDF Vectorization  
- Scikit-learn  

### 🔹 Backend
- Python  
- Fast API  

### 🔹 Frontend
- HTML  
- CSS  

### 🔹 Deployment
- Render  

---

## 🧩 ML Pipeline

1. **Text Input** – User enters email content  
2. **TF-IDF Vectorizer** – Converts text into numerical features  
3. **ML Classifier** – Predicts Spam or Not Spam  
4. **Output** – Result displayed on the web page  

---

## 📊 Dataset

- Labeled email dataset containing:
  - `spam`
  - `ham` (not spam)
- Commonly used SMS/Email spam dataset
- Text-based binary classification problem

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/mohd-musheer/email-spam-detector.git
cd email-spam-detector
