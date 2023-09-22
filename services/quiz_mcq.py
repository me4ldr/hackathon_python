
from flask import Blueprint, jsonify,  request, jsonify,send_file

import os
quiz_mcq_bp = Blueprint("quiz_mcq", __name__)

# Mock questions data
questions = [
    {
        "question": "Which gas do plants absorb from the atmosphere during photosynthesis?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correctAnswerIndex": 1
    },
    {
        "question": "Who is the author of 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy"],
        "correctAnswerIndex": 1
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Ag", "Au", "Fe", "Cu"],
        "correctAnswerIndex": 1
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "correctAnswerIndex": 1
    },
    {
        "question": "What is the largest mammal on Earth?",
        "options": ["African Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correctAnswerIndex": 1
    }
],

@quiz_mcq_bp.route("/quiz/questions", methods=["GET"])
def get_questions():
    return jsonify(questions)