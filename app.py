from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

notes = []

# Serve HTML
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# Serve CSS
@app.route("/style.css")
def style():
    return send_from_directory(".", "style.css")

# Serve JS
@app.route("/script.js")
def script():
    return send_from_directory(".", "script.js")

# Add note
@app.route("/add", methods=["POST"])
def add_note():
    data = request.get_json()
    note = data.get("text")

    if note:
        notes.append(note)
        return jsonify({"message": "Note added"})
    return jsonify({"error": "Empty note"}), 400

# Get notes
@app.route("/get")
def get_notes():
    return jsonify(notes)

if __name__ == "__main__":
    app.run(debug=True)
