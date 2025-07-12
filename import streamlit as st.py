import streamlit as st
import cv2
import face_recognition as frg
import yaml 
from utils import recognize, build_dataset
from cryptography.fernet import Fernet

st.set_page_config(layout="wide")
# Config
cfg = yaml.load(open('config.yaml','r'), Loader=yaml.FullLoader)
PICTURE_PROMPT = cfg['INFO']['PICTURE_PROMPT']
WEBCAM_PROMPT = cfg['INFO']['WEBCAM_PROMPT']

st.sidebar.title("Settings")

# Create a menu bar
menu = ["Picture", "Webcam"]
choice = st.sidebar.selectbox("Input type", menu)
# Put slide to adjust tolerance
TOLERANCE = st.sidebar.slider("Tolerance", 0.0, 1.0, 0.5, 0.01)
st.sidebar.info("Tolerance is the threshold for face recognition. The lower the tolerance, the more strict the face recognition. The higher the tolerance, the more loose the face recognition.")

# Information section 
st.sidebar.title("Student Information")
name_container = st.sidebar.empty()
id_container = st.sidebar.empty()
name_container.info('Name: Unknown')
id_container.success('ID: Unknown')

authenticated = False
user_name = None
user_id = None

if choice == "Picture":
    st.title("Face Recognition App")
    st.write(PICTURE_PROMPT)
    uploaded_images = st.file_uploader("Upload", type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)
    if len(uploaded_images) != 0:
        for image in uploaded_images:
            img = frg.load_image_file(image)
            img, name, id = recognize(img, TOLERANCE)
            name_container.info(f"Name: {name}")
            id_container.success(f"ID: {id}")
            st.image(img)
            if name != "Unknown":
                authenticated = True
                user_name = name
                user_id = id
    else:
        st.info("Please upload an image")

elif choice == "Webcam":
    st.title("Face Recognition App")
    st.write(WEBCAM_PROMPT)
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    FRAME_WINDOW = st.image([])
    while True:
        ret, frame = cam.read()
        if not ret:
            st.error("Failed to capture frame from camera")
            st.info("Please turn off the other app that is using the camera and restart app")
            st.stop()
        img, name, id = recognize(frame, TOLERANCE)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        name_container.info(f"Name: {name}")
        id_container.success(f"ID: {id}")
        FRAME_WINDOW.image(img)
        if name != "Unknown":
            authenticated = True
            user_name = name
            user_id = id
            break

# Secure message/file transfer section (after authentication)
if authenticated:
    st.success(f"Authenticated as {user_name} (ID: {user_id})")
    st.header("Secure Message/File Transfer")
    key = Fernet.generate_key()
    fernet = Fernet(key)
    st.write("Encryption key (keep this safe to decrypt):")
    st.code(key.decode(), language="text")

    file_to_send = st.file_uploader("Upload a file to encrypt and send", type=None)
    message_to_send = st.text_area("Or enter a message to encrypt and send")

    if file_to_send is not None:
        file_bytes = file_to_send.read()
        encrypted_file = fernet.encrypt(file_bytes)
        st.download_button("Download Encrypted File", encrypted_file, file_name="encrypted_file.bin")
    elif message_to_send:
        encrypted_message = fernet.encrypt(message_to_send.encode())
        st.download_button("Download Encrypted Message", encrypted_message, file_name="encrypted_message.bin")

with st.sidebar.form(key='my_form'):
    st.title("Developer Section")
    submit_button = st.form_submit_button(label='REBUILD DATASET')
    if submit_button:
        with st.spinner("Rebuilding dataset..."):
            build_dataset()
        st.success("Dataset has been reset")