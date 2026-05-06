from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store notes in memory
notes = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_note():
    data = request.get_json()
    note = data.get("text")

    if note:
        notes.append(note)
        return jsonify({"message": "Note added"})
    else:
        return jsonify({"error": "Empty note"}), 400

@app.route("/get", methods=["GET"])
def get_notes():
    return jsonify(notes)

if __name__ == "__main__":
    app.run(debug=True)