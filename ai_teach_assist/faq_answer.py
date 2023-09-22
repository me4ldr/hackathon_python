import os
from sentence_transformers import SentenceTransformer, util
from ai_teach_assist.loader import load_json
# os.environ['CURL_CA_BUNDLE'] = ''


class FAQ:
    """
    AI teaching Assistant (Instructor) - FAQ: answer basic questions related to courses content
    """
    def __init__(self):
        self.model_path = os.path.join(os.path.dirname(__file__), 'models')
        self.model = None
        self.local_embeddings = []

        self.load_model()
        self.load_question_answer_mapper()

    def load_question_answer_mapper(self):
        mapper = load_json(os.path.join(
            os.path.dirname(__file__), 'data', 'question_answer_mapper.json'))
        questions = [item['question'] for item in sum(mapper.values(), [])]
        answers = [[item['answer']] * len(item['question']) for item in sum(mapper.values(), [])]
        self.questions = sum(questions, [])
        self.answers = sum(answers, [])

    def answer(self, query):
        # Compute embedding for both lists
        embeddings1 = self.model.encode(query * len(self.questions), convert_to_tensor=True)
        embeddings2 = self.model.encode(self.questions, convert_to_tensor=True)

        # Compute cosine-similarities
        cosine_scores = util.cos_sim(embeddings1, embeddings2)[0]

        results = sorted(zip(cosine_scores, self.questions, self.answers), reverse=True)[0]
        return results

    def load_model(self):
        print('\t Start loading embedding model...')
        self.model = SentenceTransformer(os.path.join(self.model_path, 'sentence-transformers_sentence-t5-base'))
        print('\t Model Loaded...')


# if __name__ == "__main__":
#     # Download sentences bert model, please run first time using FAQ module
#     from sentence_transformers import SentenceTransformer
#
#     sentences = ["This is an example sentence", "Each sentence is converted"]
#
#     modelPath = os.path.join(
#             os.path.dirname(__file__), 'models')
#
#     model = SentenceTransformer('sentence-transformers/sentence-t5-base')
#     model.save(modelPath)
#     embeddings = model.encode(sentences)
#     print(embeddings)
