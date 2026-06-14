#  Face Landmark Detection System

## 📌 Overview

The Face Landmark Detection System is a Computer Vision application that detects human faces in uploaded images and identifies important facial landmarks such as:

* 👁 Left Eye
* 👁 Right Eye
* 👃 Nose
* 👄 Mouth

The application uses OpenCV for face detection and MediaPipe Face Mesh for facial landmark localization. A bounding box is drawn around each detected face, and key landmarks are highlighted on the image.

---

## 🌐 Live Demo

The application is deployed using Streamlit Community Cloud.

🔗 **Live Application:**


---

## 🚀 Features

✅ Upload image through Streamlit interface

✅ Face Detection using OpenCV Haar Cascade

✅ Facial Landmark Detection using MediaPipe Face Mesh

✅ Detects:

* Left Eye
* Right Eye
* Nose
* Mouth

✅ Draws Bounding Box around detected face

✅ Displays Detection Summary

✅ Download Processed Image

✅ Clean and Interactive User Interface

---

## 🛠 Technologies Used

* Python
* OpenCV
* MediaPipe
* Streamlit
* NumPy
* Pillow

---

## 📂 Project Structure

```text
Face-Landmark-Detection-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── images/
│   └── app_icon.png
│   ├── home_page.png
│   ├── detection_result.png
│   └── detection_summary.png
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
https://github.com/bantucharuhaasini-cmd/Face-Landmark-Detection-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Face-Landmark-Detection-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```
---

## 📊 Workflow

1. Upload an Image
2. Detect Face(s)
3. Generate Face Bounding Box
4. Detect Facial Landmarks
5. Display Processed Image
6. Show Detection Summary
7. Download Processed Result

---

## 📸 Screenshots

### 🏠 Home Page

Upload interface before selecting an image.

```markdown
images/home_page.png
```

---

### ✅ Face Detection Result

Detected face with bounding box and facial landmarks.

```markdown
images/detection_result.png
```

---

### 📊 Detection Summary

Displays the number of faces detected and available features.

```markdown
images/detection_summary.png
```

---

## 📱 Access

The deployed application allows users to:

* Upload facial images
* Detect faces automatically
* Identify facial landmarks
* View detection results instantly
* Download processed images

without installing any software locally.

---

## 🎯 Applications

* Face Analysis
* Facial Feature Detection
* Human-Computer Interaction
* Attendance Systems
* Identity Verification
* Computer Vision Research
* AI-Based Vision Applications

---

## 🔮 Future Enhancements

* Webcam Support
* Real-Time Landmark Tracking
* Face Recognition
* Emotion Detection
* Head Pose Estimation
* Multiple Face Analytics
* Face Mask Detection

---

## 👩‍💻 Author

**Charu Haasini Bantu**


