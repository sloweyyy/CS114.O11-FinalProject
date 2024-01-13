import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from joblib import dump, load
import gradio as gr
from PIL import Image
import cv2
import pandas as pd
import dlib

# Load data
data = pd.read_csv("dataset.csv")

# Split data
x = data.drop("label", axis=1)
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Scale data
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train SVM model
svm_model = SVC(C=0.1, gamma=0.1, kernel='linear', probability=True)
svm_model.fit(X_train_scaled, y_train)

# Evaluate model
y_pred = svm_model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average=None)
recall = recall_score(y_test, y_pred, average=None)
f1 = f1_score(y_test, y_pred, average=None)

# Save model
dump(svm_model, 'svm_model.joblib')

# Gradio interface
emotion_labels = {
    0: "Angry",
    1: "Fear",
    2: "Sad",
    3: "Neutral",
    4: "Happy",
}

detector = dlib.get_frontal_face_detector()

def predict_emotion(image):
    img_array = np.array(image)
    processed_image = Image.fromarray(img_array).convert('L').resize((48, 48))
    processed_image_array = np.array(processed_image)
    flattened_img = processed_image_array.flatten().reshape(1, -1) / 255.0
    prediction = svm_model.predict(flattened_img)[0]
    
    faces = detector(img_array, 1)
    cropped_face = img_array if len(faces) == 0 else img_array[faces[0].top():faces[0].bottom(), faces[0].left():faces[0].right()]

    return emotion_labels[prediction], cropped_face

iface = gr.Interface(
    fn=predict_emotion,
    inputs="image",
    outputs=["text", "image"],
    title="Emotion Detection",
    description="Upload an image and predict the emotion."
)

iface.launch()
