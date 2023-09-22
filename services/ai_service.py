import os
import nltk
from flask import Blueprint, request
from flask import jsonify

from ai_teach_assist.faq_answer import FAQ
from ai_teach_assist.gpt_cosplay import GPTCosplayTaskReviewer, GPTCosplayTaskGenerator
from ai_teach_assist.loader import FileLoader

ai_service = Blueprint('ai_service', __name__)

# nltk 模型存储路径
NLTK_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "ai_teach_assist", "data", "nltk_data")

nltk.data.path.append(NLTK_DATA_PATH)

ASSIGNMENT_PATH = os.path.join(os.path.dirname(__file__), "..", "assignments")
ANSWER_PATH = os.path.join(os.path.dirname(__file__), "..", "assignments")

GPT_API_KEY = ''
# # # # # only for local usage
# os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
# os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
# os.environ['ALL_PROXY'] = 'http://127.0.0.1:7890'

# Load Models first for FAQ
faq_service = FAQ()


# @ai_service.route('/ai_service/', methods=['POST'])
# def ai_service():
#     return 'welcome to my ai_service!', 200


@ai_service.route('/api/ai_service/faq', methods=['POST'])
def auto_answer():
    data = request.get_json()
    query = data['query']
    sim_score, sim_question, answer = faq_service.answer(query)
    print(sim_score)
    if sim_score > 0.85:
        return jsonify({'code':200,'answer': answer})
    else:
        return jsonify({'code':200,'answer': 'Oops, sorry, AI TA can not answer this question.'})


@ai_service.route('/ai_service/auto_review', methods=['GET'])
def auto_review():
    # data = request.get_json()
    # question_path, answer_path = data['question_path'], data['answer_path']
    question_path, answer_path = 'quiz1_question.pdf', 'quiz1_answer.png'

    question = FileLoader(file_path=os.path.join(ASSIGNMENT_PATH, question_path)).load()
    answer = FileLoader(file_path=os.path.join(ANSWER_PATH, answer_path)).load()

    mark, comment = GPTCosplayTaskReviewer(question=question, answer=answer).process(api_key=GPT_API_KEY)

    task_path = os.path.join(ASSIGNMENT_PATH, 'review_result.txt')

    with open(task_path, 'w') as f:
        f.write('Mark: ' + mark + '\nComment: ' + comment)

    return jsonify({'mark': mark, 'comment': comment}), 200


@ai_service.route('/ai_service/auto_generate', methods=['POST'])
def generate_assignment():
    data = request.get_json()
    topic = data['quizQuestion']

    question = GPTCosplayTaskGenerator(topic=topic).process(api_key=GPT_API_KEY)
    task_path = os.path.join(ASSIGNMENT_PATH, 'quiz_ai_generate.txt')

    with open(task_path, 'w') as f:
        f.write(question)

    return jsonify({'quiz': question}), 200
