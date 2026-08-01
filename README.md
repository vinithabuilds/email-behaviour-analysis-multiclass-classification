# Email Behaviour Analysis and Multi-Class Email Classification System

A machine learning-based desktop application that classifies email messages into **Spam**, **Ham**, and **Phish** using behavioural feature engineering, TF-IDF vectorization, and a Multinomial Naive Bayes classifier. The application provides real-time predictions with confidence scores through an interactive Tkinter GUI and includes MySQL integration and Power BI visualization.

---

## Project Overview

This project combines Natural Language Processing (NLP), Machine Learning, and behavioural feature engineering to improve email classification beyond traditional keyword-based filtering. It analyzes both textual and behavioural characteristics of email messages to accurately classify them as **Spam**, **Ham**, or **Phish**.

---

## Features

- Multi-class email classification (Spam, Ham, and Phish)
- Behavioural feature engineering
- TF-IDF character n-gram vectorization
- Machine learning using Multinomial Naive Bayes
- Predicts the email category with confidence score
- Interactive Tkinter desktop application (GUI)
- Model evaluation using a Classification Report and Confusion Matrix
- Confusion Matrix visualized as a heatmap
- MySQL database integration
- Power BI dashboard for data visualization

---

## Technologies Used

- Python
- Tkinter
- Pandas
- NumPy
- Scikit-learn
- SciPy
- Matplotlib
- Seaborn
- SQLAlchemy
- PyMySQL
- MySQL
- Power BI
- Pickle
- Regular Expressions (`re`)

---

## Machine Learning Workflow

1. Data preprocessing
2. Text cleaning using Regular Expressions (`re`)
3. Behavioural feature engineering
4. TF-IDF character n-gram feature extraction
5. Feature scaling using MinMaxScaler
6. Model training using Multinomial Naive Bayes
7. Model evaluation
8. Model persistence using Pickle
9. Email prediction with confidence score
10. Desktop GUI deployment using Tkinter

---

## Model Performance

- **Test Accuracy:** **97.2%**
- Evaluated using a Classification Report
- Confusion Matrix visualization using a heatmap
- Confidence score displayed for every prediction

---

## Project Structure

- Dataset preprocessing
- Feature engineering
- Machine learning model training
- Trained model files (`.pkl`)
- Tkinter desktop application
- MySQL database integration
- Power BI dashboard

---

## Future Enhancements

- Deploy the application as a web application using FastAPI
- Integrate real-time email analysis
- Experiment with advanced machine learning and deep learning models
- Deploy the application to the cloud

---

## Author

**M. Vinitha** 
GitHub: @vinithabuilds
