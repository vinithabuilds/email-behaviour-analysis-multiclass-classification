import tkinter as tk
from tkinter import messagebox
import pickle
import re
import numpy as np
from scipy.sparse import hstack

# ---------------- LOAD MODEL, VECTORIZER, SCALER ----------------
with open("spam_model_v3.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer_v3.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("scaler_v3.pkl", "rb") as f:
    scaler = pickle.load(f)

# ---------------- PHISH & SPAM PHRASES ----------------
phish_phrases = [
    "verify account", "update bank", "click here",
    "confirm identity", "password reset", "refund pending",
    "bank alert", "update account", "account suspended",
    "unusual activity", "security alert", "reset password",
    "click the link", "login immediately", "bank details",
    "credit card issue", "otp verification", "claim your prize"
]

spam_phrases = [
    "limited time offer", "buy now", "free trial",
    "exclusive deal", "don't miss out", "mega sale",
    "get discount", "70% off", "coupon code",
    "flash sale", "apply code now", "congratulations you won",
    "winner", "free gift", "last chance",
    "click here immediately", "limited stock",
    "download today", "trial expires",
    "shop today", "order now", "urgent message",
    "flash offer"
]

# ---------------- TEXT CLEANING ----------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# ---------------- BEHAVIORAL FEATURES ----------------
def extract_behaviour_features(text):
    cleaned = clean_text(text)
    
    char_length = len(cleaned)
    word_count = len(cleaned.split())
    sentence_count = len(re.findall(r'[.!?]+', cleaned))
    url_count = len(re.findall(r'http[s]?://', cleaned))
    digit_count = sum(c.isdigit() for c in cleaned)
    uppercase_count = sum(c.isupper() for c in text)
    special_char_count = len(re.findall(r'[^\w\s]', text))

    phish_score = 2 * sum(p in cleaned for p in phish_phrases)

    spam_score = 2 * sum(p in cleaned for p in spam_phrases)
    
    features = np.array([
        char_length,
        word_count,
        sentence_count,
        url_count,
        digit_count,
        uppercase_count,
        special_char_count,
        phish_score,
        spam_score
    ]).reshape(1, -1)
    
    return features

# ---------------- PREDICTION FUNCTION ----------------
def predict_message(msg):
    cleaned = clean_text(msg)
    text_vector = vectorizer.transform([cleaned])
    
    behaviour_features = extract_behaviour_features(msg)
    behaviour_features_scaled = scaler.transform(behaviour_features)  # scale behavioral features
    
    X_final = hstack([text_vector, behaviour_features_scaled])
    
    pred = model.predict(X_final)[0]
    pred_proba = model.predict_proba(X_final)
    confidence = np.max(pred_proba) * 100
    
    return pred, confidence

# ---------------- GUI FUNCTIONS ----------------
def on_predict():
    msg = text_input.get("1.0", tk.END).strip()
    if not msg:
        messagebox.showwarning("Input Error", "Please enter an email message to predict.")
        return
    try:
        pred, confidence = predict_message(msg)
        result_label.config(text=f"Prediction: {pred.upper()} | Confidence: {confidence:.2f}%")
    except Exception as e:
        messagebox.showerror("Prediction Error", str(e))

def on_clear():
    text_input.delete("1.0", tk.END)
    result_label.config(text="Prediction: ")

# ---------------- GUI LAYOUT ----------------
root = tk.Tk()
root.title("Email Behaviour Analysis System")
root.geometry("650x450")

tk.Label(root, text="Enter Email Message:", font=("Arial", 14)).pack(pady=10)
text_input = tk.Text(root, height=12, width=80)
text_input.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

predict_btn = tk.Button(btn_frame, text="Predict", command=on_predict, width=20, bg="lightgreen")
predict_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear", command=on_clear, width=20, bg="lightcoral")
clear_btn.grid(row=0, column=1, padx=10)

result_label = tk.Label(root, text="Prediction: ", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()