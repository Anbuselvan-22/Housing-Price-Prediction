# 🏠 Housing Price Prediction Web App

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)  [![Flask](https://img.shields.io/badge/Flask-1.1.2-orange?logo=flask)](https://flask.palletsprojects.com/)  [![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.24-green?logo=scikit-learn)](https://scikit-learn.org/)  [![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5)](https://developer.mozilla.org/en-US/docs/Web/HTML)  [![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3)](https://developer.mozilla.org/en-US/docs/Web/CSS)  [![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  [![Live Demo](https://img.shields.io/badge/Live%20Demo-View-green)](https://your-live-demo-link.com)  

---

## 🔥 Overview

A **Machine Learning web application** that predicts **housing prices** based on property features.  

Users can enter details like:  

- 🏡 Area  
- 🛏 Bedrooms  
- 🛁 Bathrooms  
- 🏢 Stories  
- 🛣 Main Road, Guest Room, Basement, etc.  

…and get an **instant price estimate**. 

---

## ✅ Features

- 🖥 Predict house prices using a **trained ML model**  
- 🎨 Clean and responsive **web interface**  
- 🏷 Handles categorical features: **Furnishing Status, Main Road, Guest Room**  
- ⚡ **Instant prediction** on form submission  
- 🔧 Built with **Flask backend + HTML/CSS frontend**  

---

## 📊 Dataset

| Feature | Type | Description |
|---------|------|-------------|
| price | Numeric | House price in INR (target) |
| area | Numeric | Area in sq ft |
| bedrooms | Numeric | Number of bedrooms |
| bathrooms | Numeric | Number of bathrooms |
| stories | Numeric | Number of floors |
| mainroad | Binary | 1 if on main road, 0 otherwise |
| guestroom | Binary | 1 if guest room exists, 0 otherwise |
| basement | Binary | 1 if basement exists, 0 otherwise |
| hotwaterheating | Binary | 1 if hot water heating exists, 0 otherwise |
| airconditioning | Binary | 1 if air conditioning exists, 0 otherwise |
| parking | Numeric | Number of parking spots |
| prefarea | Binary | 1 if in preferred area, 0 otherwise |
| furnishingstatus | Categorical | 2: Furnished, 1: Semi-Furnished, 0: Unfurnished |

---

## 💻 Tech Stack

- **Backend:** Python, Flask  
- **Machine Learning:** Scikit-learn  
- **Frontend:** HTML5, CSS3  
- **Model Storage:** Pickle (`model.pkl`)  

---

## ⚡ Installation

1. Clone repository:  
```bash
git clone https://github.com/yourusername/housing-price-prediction.git
cd housing-price-prediction
Create virtual environment:
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
Install dependencies:
pip install -r requirements.txt
Run the app:
python app.py
Open browser at:
http://127.0.0.1:5000 
```
---
## 🚀 Usage
- Enter house details: area, bedrooms, bathrooms, stories, etc.
- Click Predict Price
- The predicted price is displayed instantly below the form
___
## 🗂 Folder Structure
```bash

housing-price-prediction/
│
├── app.py                  # Flask backend
├── model.pkl               # Trained ML model
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend HTML
├── static/
│   └── style.css           # CSS styling
└── README.md               # Project documentation
```
___

## 💡 Future Improvements
- 📊 Add charts comparing predicted vs actual prices
- 📈 Show R², MAE, RMSE metrics on the UI
- 🗂 Batch prediction via CSV upload
- 🌐 Deploy on Render / Railway / Heroku

---

## 📜 License
```bash
This project is open-source under the MIT License.
