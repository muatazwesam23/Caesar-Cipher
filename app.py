from flask import Flask, render_template, request
import os

app = Flask(__name__)

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            shifted = chr((ord(char) - offset + shift) % 26 + offset)
            result += shifted
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ""
    plaintext = ""
    shift = 3  # default shift

    if request.method == 'POST':
        plaintext = request.form.get('plaintext', '')
        shift_value = request.form.get('shift', '3')
        try:
            shift = int(shift_value)
            encrypted_text = caesar_encrypt(plaintext, shift)
        except:
            encrypted_text = "Invalid shift value"

    return render_template('index.html', encrypted=encrypted_text, plaintext=plaintext, shift=shift)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
