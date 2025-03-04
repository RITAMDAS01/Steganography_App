from flask import Flask, render_template, request, send_file, redirect, url_for
import os
import sqlite3
from datetime import datetime
from steganography import encrypt_image, decrypt_image

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# DB Setup
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, filename TEXT, action TEXT, time TEXT)''')
    conn.commit()
    conn.close()
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    image = request.files['image']
    message = request.form['message']
    password = request.form['password']
    filename = os.path.join(UPLOAD_FOLDER, image.filename)
    encrypted_filename = os.path.join(UPLOAD_FOLDER, 'encrypted_' + image.filename)
    image.save(filename)

    encrypt_image(filename, message, password, encrypted_filename)

    log('encrypted_' + image.filename, 'ENCRYPT')

    return send_file(encrypted_filename, as_attachment=True)

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        image = request.files['image']
        password = request.form['password']
        filename = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(filename)

        message = decrypt_image(filename, password)
        log(image.filename, 'DECRYPT')
        return render_template('decrypt.html', message=message)

    return render_template('decrypt.html', message=None)

def log(filename, action):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO logs (filename, action, time) VALUES (?, ?, ?)',
              (filename, action, datetime.now()))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    app.run(debug=True)
