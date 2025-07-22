# 🕵️‍♂️ Steganography Web App with Password Protection


A simple Flask-based web application to **encrypt secret messages inside images** and **decrypt them using a password**. The app also logs actions to a SQLite database.

---

## 🚀 Features
- Encrypt messages into images with a password.
- Decrypt messages from images using the correct password.
- Image preview before upload.
- Password visibility toggle.
- SQLite database to log encryption and decryption actions.
- Frontend using HTML, CSS, and JavaScript.

---

## 🗂️ Project Structure

steganography_app/ │ ├── app.py ├── steganography.py ├── database.db ├── requirements.txt ├── static/ │ ├── styles.css │ └── script.js ├── templates/ │ ├── index.html │ └── decrypt.html ├── uploads/ └── README.md


---

## ⚙️ Installation & Running

### 1️⃣ Clone the project or download the ZIP
```bash
git clone <repository_link>
cd steganography_app

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Run the application

python app.py

4️⃣ Open in your browser

http://127.0.0.1:5000/

🔑 How to Use
➤ To Encrypt:

    Go to the home page.
    Upload an image.
    Enter a secret message.
    Enter a password.
    Download the encrypted image.

➤ To Decrypt:

    Go to the decrypt page.
    Upload the encrypted image.
    Enter the password.
    View the hidden message.

🗃️ Database Logging

The app logs every encryption and decryption into database.db with:

    Filename
    Action (ENCRYPT or DECRYPT)
    Timestamp

✅ Tech Stack

    Python (Flask)
    Pillow (PIL)
    SQLite
    HTML, CSS, JavaScript

⚠️ Important Notes

    Use the same password for decryption that was used for encryption.
    Works best with PNG and JPG images.
    The password is stored within the image for basic verification (not secure for sensitive data).

🔮 Future Enhancements

    Advanced encryption techniques.
    User login and authentication.
    Stronger password protection with hashing.
    Improved UI/UX design.

📝 License

Free to use for learning and educational purposes.

