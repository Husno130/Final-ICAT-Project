## OncoScan: AI-Powered Cancer Detection for Early and Accurate Diagnosis

### 🚀 **Project Overview**
OncoScan is a web-based platform that uses deep learning algorithms to detect and classify cancers from medical images. The system identifies tumors across 8 cancer types, classifying them as benign, malignant, or no tumor. This tool aims to assist healthcare providers with early diagnosis, enhancing decision-making and patient outcomes.

---

### 📊 **Features**
- **Multi-Cancer Detection:** Supports 8 cancer types (blood, brain, breast, cervical, colon, lung, oral, skin).
- **Tumor Classification:** Distinguishes between benign, malignant, and no tumor states.
- **Confidence Scores:** Provides confidence percentages for predictions.
- **User-Friendly Interface:** Simple web-based image upload and real-time predictions.
- **Educational Resources:** Awareness pages for cancer education and imaging techniques.

---

### 🛠 **Tech Stack**
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Model Framework:** TensorFlow/Keras (DenseNet)
- **Deployment Options:** Flask with Gunicorn, Docker, or cloud platforms like AWS/Render

---

### 📂 **Project Structure**
```
OncoScan/
├── static/                   # CSS, JS, images
├── templates/                # HTML templates
├── models/                  # Pre-trained model (OncoScan.h5)
├── app.py                   # Flask backend logic
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

### ⚙️ **Setup & Installation**
1. **Clone the Repository:**
```bash
git clone https://github.com/yourusername/oncoscan.git
cd oncoscan
```

2. **Create a Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate      # On Windows
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Flask App:**
```bash
python app.py
```

5. **Access the Web App:**
```
http://localhost:5000
```

---

### 🚀 **Deployment**
- **Local:** Flask with Gunicorn/Nginx
- **Containerized:** Docker for easier deployment
- **Cloud:** Render, Railway, Heroku, or AWS for global accessibility

---

### 🧠 **Model Performance**
- **Accuracy:** 93.85%
- **Loss:** 0.14366
- **Training Stability:** Accuracy plateaued around epoch 14, ensuring model reliability.

---

### 📘 **Usage Instructions**
1. **Select Cancer Type:** Choose from 8 supported cancers.
2. **Upload an Image:** Use JPG/PNG formats (resized to 224x224).
3. **Get Results:** View cancer type, malignancy status, and confidence scores.

---

### 🎯 **Future Enhancements**
- Risk estimation and lifestyle suggestions.
- Model accuracy improvements via more robust training.
- Real-time medical use integration with clinics.
- Scalability for other diseases.

---


### 📬 **Contact**
- **Team:** OncoScan AI Research Group
- **Email:** husno130@gmail.com
- **GitHub:** [@husno130](https://github.com/yourusername)

Would you like me to refine anything or add more details? Let me know! 🚀

