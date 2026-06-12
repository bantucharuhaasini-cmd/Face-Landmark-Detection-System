import streamlit as st
import cv2 as cv
import mediapipe as mp
import numpy as np

from PIL import Image

icon = Image.open("images/app_icon.jpg")

st.set_page_config(
    page_title="Face Landmark Detection System",
    page_icon=icon,
    layout="wide"
)
# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.image(icon)
st.sidebar.title("Face Landmark Detection")

st.sidebar.info(
    """
This application detects:

✅ Face Region

✅ Facial Landmarks

• Left Eye
• Right Eye
• Nose
• Mouth

Built using:
- OpenCV
- MediaPipe
- Streamlit
"""
)

# --------------------------------------------------
# Main Title
# --------------------------------------------------

st.title("Face Landmark Detection System")

st.markdown(
"""
Upload an image and the system will:

1. Detect the face
2. Draw a bounding box
3. Detect important facial landmarks
4. Display the processed image
"""
)

st.markdown("---")

# --------------------------------------------------
# Upload Image
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "📤 Upload an Image",
    type=["jpg", "jpeg", "png","webp"]
)

if uploaded_file is not None:

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    image = cv.imdecode(
        file_bytes,
        cv.IMREAD_COLOR
    )

    original = image.copy()

    # ----------------------------------------------
    # Face Detection
    # ----------------------------------------------

    face_detector = cv.CascadeClassifier(
        cv.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    gray = cv.cvtColor(
        image,
        cv.COLOR_BGR2GRAY
    )

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # ----------------------------------------------
    # MediaPipe
    # ----------------------------------------------

    mp_face_mesh = mp.solutions.face_mesh

    with mp_face_mesh.FaceMesh(
        static_image_mode=True,
        max_num_faces=5
    ) as face_mesh:

        rgb = cv.cvtColor(
            image,
            cv.COLOR_BGR2RGB
        )

        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:

            for face_landmarks in results.multi_face_landmarks:

                h, w, _ = image.shape

                landmark_ids = {
                    "Left Eye": 33,
                    "Right Eye": 263,
                    "Nose": 1,
                    "Mouth": 13
                }

                for name, idx in landmark_ids.items():

                    landmark = face_landmarks.landmark[idx]

                    x = int(landmark.x * w)
                    y = int(landmark.y * h)

                    cv.circle(
                        image,
                        (x, y),
                        30,
                        (0, 0, 255),
                        -1
                    )

                    cv.putText(
                        image,
                        name,
                        (x + 12, y - 12),
                        cv.FONT_HERSHEY_SIMPLEX,
                        1.5,
                        (255, 0, 0),
                        5
                    )

    # ----------------------------------------------
    # Bounding Boxes
    # ----------------------------------------------

    for (x, y, w, h) in faces:

        cv.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            8
        )

        cv.putText(
            image,
            "Face Detected",
            (x, y - 10),
            cv.FONT_HERSHEY_SIMPLEX,
            5.0,
            (0, 255, 0),
            9
        )

    # ----------------------------------------------
    # Display
    # ----------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🖼 Original Image")
        st.image(
            cv.cvtColor(
                original,
                cv.COLOR_BGR2RGB
            ),
            use_container_width=True
        )

    with col2:
        st.subheader("✅ Detected Image")
        st.image(
            cv.cvtColor(
                image,
                cv.COLOR_BGR2RGB
            ),
            use_container_width=True
        )

    st.markdown("---")

    st.subheader("📊 Detection Summary")

    st.success(
        f"Faces Detected: {len(faces)}"
    )

    st.info(
        """
Detected Features:

• Face Region

• Left Eye

• Right Eye

• Nose

• Mouth
"""
    )

    # ----------------------------------------------
    # Download Result
    # ----------------------------------------------

    _, buffer = cv.imencode(
        ".png",
        image
    )

    st.download_button(
        label="💾 Download Processed Image",
        data=buffer.tobytes(),
        file_name="detected_face.png",
        mime="image/png"
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Built with OpenCV, MediaPipe and Streamlit"
)