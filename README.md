# Secure Face Recognition-Based Message and File Transfer System

This is a secure face recognition application built using Python, [Face-Recognition API](https://github.com/ageitgey/face_recognition), and the Streamlit framework. The app allows users to authenticate using face recognition and then securely send messages or files using strong encryption. Only authenticated users can access the secure transfer features, ensuring privacy and data protection.

---

## Features

- Face detection and recognition (image upload or webcam)
- Multi-face recognition
- Secure message and file encryption using Fernet (AES-based)
- Unique encryption key for each transfer (required for decryption)
- User-friendly web interface
- Dataset management (add, delete, update faces)
- Database viewing and CSV export

---

## Requirements 
- Python 3.9
- Streamlit 1.22.0
- face_recognition (see requirements.txt for fork)
- OpenCV, cryptography, numpy, Pillow, PyYAML, cmake

---

## Repository Structure
```bash
├── dataset/
│   └── ID_Name.jpg
├── pages/
│   ├── 1_🔧_Updating.py
│   └── 2_💾_Database.py
├── Tracking.py
├── utils.py
├── config.yaml 
├── requirements.txt
├── packages.txt
└── README.md
```

---

## Description

- **dataset/**: Contains images of people to be recognized. File name format: `ID_Name.jpg` (e.g., `1_Elon_Musk.jpg`).
- **pages/**: Contains code for each app page (dataset management, database view).
- **Tracking.py**: Main app page for authentication and secure transfer.
- **utils.py**: Utility functions for face recognition and dataset management.
- **config.yaml**: App configuration (dataset path, prompts, etc.).
- **requirements.txt**: Python dependencies.
- **packages.txt**: Packages for deployment (e.g., Streamlit Cloud).

---

## Installation

1. **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd Face-recognition-app-using-Streamlit
    ```

2. **Install the dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**
    ```bash
    streamlit run Tracking.py
    ```

---

## Usage

1. **Authenticate using webcam or image upload**
2. **After authentication, securely send a file or message**
   - Upload a file or enter a message
   - Download the encrypted content and save the encryption key
3. **Decrypt files/messages using the provided key and a Python script**
4. **Manage the face dataset (add, delete, update) via the Updating page**
5. **View and export the face database**

---

## Decryption Example

To decrypt a file or message, use the encryption key provided by the app:

```python
from cryptography.fernet import Fernet

key = b'your-key-here'  # Replace with your actual key
fernet = Fernet(key)

# Decrypt a file
with open('encrypted_file.bin', 'rb') as f:
    encrypted = f.read()
decrypted = fernet.decrypt(encrypted)
with open('decrypted_file', 'wb') as f:
    f.write(decrypted)
```

---

## Demo

1. **Face authentication using webcam**
    ![Tracking using webcam](assets/webcam.gif) 

2. **Face authentication using image**
    ![Tracking using picture](assets/tracking.png)

3. **Adding a new person to the database**
    ![Adding new person to database](assets/adding.png)

---

## Contact

For questions or support, please contact:  
`[your-email@example.com]`

---

*This project was developed as an internship project for Exposys Data Labs.*
