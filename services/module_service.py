from flask import Blueprint, jsonify, request, jsonify, send_file

import os

module_service_bp = Blueprint("module_service", __name__)

# Mock data for grades and comments
mock_grades = {
    'module1': 'A',
    'module2': 'B',
    'module3': 'C',
}

mock_comments = {
    'module1': 'Great work!',
    'module2': 'Good effort.',
    'module3': 'Needs improvement.',
}

# Sample data (you should replace this with a database)
modules = [
    {
        "id": 1,
        "mname": "Module A",
        "progress": 50,
        "description": "This is a sample module description",
        "lessons": [
            {"id": 1, "lname": "Lesson 1", "information": "information 1"},
            {"id": 2, "lname": "Lesson 2", "information": "information 1"},
            {"id": 3, "lname": "Lesson 3", "information": "information 1"},
            {"id": 4, "lname": "Lesson 4", "information": "information 1"},
            {"id": 5, "lname": "Lesson 5", "information": "information 1"},
        ],
    }
]


@module_service_bp.route('/grades', methods=['GET'])
def get_grades():
    return jsonify({'grades': mock_grades})


@module_service_bp.route('/comments', methods=['GET'])
def get_comments():
    return jsonify({'comments': mock_comments})


@module_service_bp.route("/api/modules/<int:module_id>")
def get_module(module_id):
    module = next((m for m in modules if m["id"] == module_id), None)
    if module:
        return jsonify(module)
    else:
        return jsonify({"error": "Module not found"}), 404


@module_service_bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        # Process the uploaded file here (e.g., save it to a directory)
        file.save('assignments' + file.filename)
        return jsonify({'message': 'File uploaded successfully'})
    else:
        return jsonify({'error': 'No file provided'}), 400


@module_service_bp.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        # Define the path to the folder where your text files are stored
        folder_path = 'assignments'
        file_path = os.path.join(folder_path, filename)

        # Use Flask's send_file method to send the file for download
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        return 'File not found', 404


# Define a route to handle quiz generation requests
@module_service_bp.route('/generate_quiz', methods=['POST'])
def generate_quiz():
    try:
        # Get the quiz question from the request
        quiz_question = request.json.get('quizQuestion')

        # Implement your quiz generation logic here based on the quiz_question
        # For simplicity, we'll just return a placeholder response.
        quiz = generate_quiz_from_question(quiz_question)

        return jsonify({'quiz': quiz})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Placeholder function for generating a quiz (replace with your logic)
def generate_quiz_from_question(question):
    # Replace this with your actual quiz generation logic
    return f"Quiz for question: {question}"
