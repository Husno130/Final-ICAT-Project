from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load Unified Multi-Cancer Model
MODEL_PATH = "models\OncoScan.h5"
model = tf.keras.models.load_model(MODEL_PATH, compile=False)

# Define cancer types and class mapping
CANCER_TYPES = ["blood", "brain", "breast", "cervical", "colon", "lung", "oral", "skin"]
CLASS_STATES = ["benign", "malignant", "no tumor"]
NUM_CLASSES = 22

# Explicit class mapping based on your labels
CLASS_MAPPING = {
    0: ("blood", "benign"), 1: ("blood", "malignant"), 2: ("blood", "no tumor"),
    3: ("brain", "benign"), 4: ("brain", "malignant"), 5: ("brain", "no tumor"),
    6: ("breast", "benign"), 7: ("breast", "malignant"), 8: ("breast", "no tumor"),
    9: ("cervical", "benign"), 10: ("cervical", "malignant"),
    11: ("colon", "benign"), 12: ("colon", "malignant"),
    13: ("lung", "benign"), 14: ("lung", "malignant"), 15: ("lung", "no tumor"),
    16: ("oral", "benign"), 17: ("oral", "malignant"), 18: ("oral", "no tumor"),
    19: ("skin", "benign"), 20: ("skin", "malignant"), 21: ("skin", "no tumor")
}

def decode_prediction(prediction):
    """Decode the 22-class softmax output into cancer type and state."""
    predicted_class = np.argmax(prediction)
    cancer_type, state = CLASS_MAPPING[predicted_class]
    confidence = prediction[0][predicted_class] * 100
    
    return cancer_type, state, confidence

# Function to preprocess image
def preprocess_image(image, target_size=(224, 224)):
    image = image.resize(target_size)
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# ROUTES FOR PAGES
@app.route("/")
def homepage():
    return render_template("Homepage.html")

@app.route("/about")
def about():
    return render_template("Aboutus.html")

@app.route("/awareness")
def awareness():
    return render_template("Awareness.html")

@app.route("/upload")
def upload_page():
    return render_template("index.html")

@app.route("/imagetechn")
def imagetechn():
    return render_template("Imagetechn.html")

# IMAGE PREDICTION ROUTE
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    try:
        # Load and preprocess image
        image = Image.open(file).convert("RGB")
        image = preprocess_image(image)

        # Model prediction
        prediction = model.predict(image)  # Shape: (1, 22)

        # Decode the prediction
        cancer_type, state, confidence = decode_prediction(prediction)

        # Adjust JSON keys to match your frontend expectation
        return jsonify({
            "cancer_type": cancer_type,
            "cancer_type_confidence": round(float(confidence), 2),
            "malignancy": state,  # Rename to "malignancy" for consistency with your original code
            "malignancy_confidence": round(float(confidence), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)