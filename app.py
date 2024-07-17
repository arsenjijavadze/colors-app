from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary storage for palette
palettes = []

@app.route('/')
def home():
    return "Welcome to the Colors App API!"

@app.route('/palettes', methods=['GET'])
def get_palettes():
    return jsonify(palettes), 200

@app.route('/palettes', methods=['POST'])
def add_palette():
    palette = request.json
    palettes.append(palette)
    return jsonify(palette), 201

if __name__ == '__main__':
    app.run(debug=True)
