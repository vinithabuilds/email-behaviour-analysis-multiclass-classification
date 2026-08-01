# Email Behaviour Analysis and Multi-Class Email Classification System

A machine learning-based desktop application that classifies email messages into **Spam**, **Ham**, and **Phish** using Natural Language Processing (NLP), behavioural feature engineering, TF-IDF vectorization, and a Multinomial Naive Bayes classifier.

The system provides real-time email classification with confidence scores through an interactive Tkinter GUI and includes MySQL integration for processed data analysis and Power BI visualization.

---

## Project Overview

Email-based threats such as spam and phishing continue to be a major cybersecurity concern. Traditional keyword-based filtering methods may fail to capture complex patterns in email content.

This project develops a **Multi-Class Email Classification System** that analyzes both textual information and behavioural characteristics of emails to classify them into:

- **Spam** – Unwanted or malicious promotional emails
- **Ham** – Legitimate emails
- **Phish** – Phishing-related suspicious emails

The project combines Natural Language Processing, Machine Learning, feature engineering, database integration, and desktop application development into a complete end-to-end system.

---

## Key Features

- Multi-class email classification (Spam, Ham, and Phish)
- Behavioural feature extraction from email content
- TF-IDF character n-gram based text feature extraction
- Multinomial Naive Bayes classification model
- Confidence score generation for predictions
- Tkinter-based interactive desktop GUI application
- Model evaluation using classification report and confusion matrix
- MySQL database integration for storing and querying processed data
- Power BI dashboard for visualization and analysis

---

## Behavioural Features Extracted

Along with textual features, the system extracts behavioural patterns from emails:

- Character length
- Word count
- Sentence count
- Suspicious phrase count
- URL count
- Digit count
- Uppercase character count
- Special character count
- Spam score
- Phishing score

These behavioural features are combined with TF-IDF features to improve classification performance.

---

## Dataset Details

The dataset contains **6,299 email records** belonging to three categories:

| Category | Records |
|----------|---------|
| Ham | 4,828 |
| Spam | 765 |
| Phish | 706 |

---

## Technologies Used

### Programming Language
- Python

### Machine Learning & Data Processing
- Pandas
- NumPy
- Scikit-learn
- SciPy

### NLP & Feature Engineering
- TF-IDF Vectorization
- Regular Expressions (`re`)
- Character n-gram analysis

### Visualization
- Matplotlib
- Seaborn
- Power BI

### Database
- MySQL
- SQLAlchemy
- PyMySQL

### Application Development
- Tkinter

### Model Persistence
- Pickle

---

## Machine Learning Workflow

1. Dataset loading and exploration
2. Data preprocessing and cleaning
3. Text cleaning using Regular Expressions
4. Behavioural feature extraction
5. TF-IDF character n-gram feature extraction
6. Behavioural feature scaling using MinMaxScaler
7. Combining text and behavioural features
8. Training using Multinomial Naive Bayes classifier
9. Model evaluation
10. Saving trained model components using Pickle
11. Loading saved models for prediction
12. Deploying prediction functionality through Tkinter GUI

---

## Model Performance

The trained model achieved:

**Test Accuracy: 97.2%**

### Evaluation Methods:

- Classification Report
  - Precision
  - Recall
  - F1-score

- Confusion Matrix
  - Visualized using a heatmap
  - Used to analyze prediction performance across Spam, Ham, and Phish categories

---

## MySQL Database Integration

The project integrates MySQL to store and analyze the processed email dataset.

### Database Workflow:

1. The original dataset (`spam mail.csv`) is loaded and processed using Python.
2. Data cleaning and behavioural feature extraction are performed.
3. The processed dataset is connected to MySQL using:
   - SQLAlchemy
   - PyMySQL
4. The cleaned data is stored in a MySQL database table.
5. SQL queries are used for data analysis and extracting insights.
6. The data is visualized using Power BI dashboards.

---

## Tkinter Desktop Application

The project includes a GUI application developed using Tkinter.

Users can:

- Enter email content
- Click the prediction button
- View the predicted category
- View the confidence score
- Clear input and perform new predictions

### Application Preview

![Email Classifier GUI](email_classifier_gui.png)

---

## Project Structure

Email-Behaviour-Analysis/ │ ├── Email_Behaviour_Analysis.ipynb ├── email_tk.py ├── spam mail.csv ├── spam_model_v3.pkl ├── tfidf_vectorizer_v3.pkl ├── scaler_v3.pkl ├── requirements.txt ├── email_classifier_gui.png └── README.md


---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Email-Behaviour-Analysis

2. Install Dependencies

pip install -r requirements.txt

3. Run the Jupyter Notebook

jupyter notebook Email_Behaviour_Analysis.ipynb

The notebook contains:
Dataset analysis
Data preprocessing
Feature engineering
Model training
Model evaluation
Saving trained model files

4. Configure MySQL Database

Install and start MySQL Server.
Create a database:

CREATE DATABASE email_analysis;

Update the MySQL connection details in the notebook:

mysql+pymysql://username:password@localhost/email_analysis

Run the database integration section to upload the processed dataset into MySQL.

### 5. Run the GUI Application

python email_tk.py

The desktop application will launch and allow users to classify email messages.

---

## Project Status

Completed

---

## Future Enhancements

- Convert the desktop application into a web application
- Develop API-based prediction services using FastAPI
- Integrate real-time email analysis capabilities
- Experiment with advanced machine learning and deep learning models
- Deploy the application on cloud platforms

---

## Author

**M. Vinitha** 
GitHub: @vinithabuilds
