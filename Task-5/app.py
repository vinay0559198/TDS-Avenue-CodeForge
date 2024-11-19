import os
from flask import Flask, request, render_template, redirect, url_for
import cv2
import face_recognition
import numpy as np

app = Flask(__name__)

# Directory containing known images
KNOWN_IMAGES_DIR = r'C:\Users\DELL\Desktop\1\Task-5\known_images'

# Load known faces
def load_known_images():
    known_encodings = []
    known_names = []
    for filename in os.listdir(KNOWN_IMAGES_DIR):
        if filename.endswith('.png'):
            image_path = os.path.join(KNOWN_IMAGES_DIR, filename)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(filename)[0])  # Use filename (without extension) as name
    return known_encodings, known_names

known_encodings, known_names = load_known_images()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    
    # Save the uploaded image
   # image_path = os.path.join('static', 'temp_image.jpg')
   # image_path = os.path.join(os.path.expanduser("~"), r'C:\Users\DELL\Desktop\1\face_recognition_app\static\temp_image.jpg')
    image_path = os.path.join(os.path.expanduser("~"), "Desktop", "temp_image.jpg")

    file.save(image_path)
    
    # Recognize faces in the uploaded image
    results = recognize_faces_in_image(image_path)
    return render_template('index.html', results=results)

def recognize_faces_in_image(image_path):
    unknown_image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    results = []
    for encoding in face_encodings:
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]
        results.append(name)

    return results

if __name__ == '__main__':
    app.run(debug=True)
