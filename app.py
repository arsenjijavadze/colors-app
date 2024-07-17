from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Temporary storage for palette
palettes = []

@app.route('/')
def home():
    return "Welcome to the Colors App API!"

@app.route('/palettes', methods=['GET', 'POST'])
def manage_palettes():
    if request.method == 'POST':
        palette = request.json.get('palette')
        if palette:
            palettes.append(palette)
            return jsonify({"message": "Palette added successfully!"}), 201 
        return jsonify({"message": "No palette provided"}), 400
    elif request.method == 'GET':
        return jsonify(palettes)

if __name__ == '__main__':
    context = ('localhost.pem', 'localhost-key.pem')
    app.run(debug=True, ssl_context=context)
