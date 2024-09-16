import os
import tempfile
from flask import Flask, request, jsonify
import yaml
from src.feedback_system import AIFeedbackSystem

app = Flask(__name__)

with open('config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

feedback_system = AIFeedbackSystem(config)


@app.route("/evaluate_notebook", methods=['POST'])
def evaluate_notebook():

    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    notebook_file = request.files['file']

    if notebook_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        notebook_file.save(temp_file.name)
        notebook_path = temp_file.name

    response = feedback_system.evaluate_notebook(notebook_path)

    os.remove(notebook_path)  # Remove the temporary file after evaluation

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
