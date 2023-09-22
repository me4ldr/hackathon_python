import os
import re
import openai
import pandas as pd


class GPTCosplay:

    def __init__(self, actor):

        self.act_role = actor
        role_prompts_df = pd.read_csv(
            os.path.join(os.path.dirname(__file__), 'data', 'chatgpt-prompts.csv'),
            encoding_errors='ignore')
        self.role_prompts = {r: p for r, p in zip(role_prompts_df['act'], role_prompts_df['prompt'])}
        self.prompt = self.role_prompts[actor]

    def process(self, api_key, model='gpt-3.5-turbo'):
        messages = [{'role': 'user', 'content': self.prompt}]

        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model=model, messages=messages, temperature=0
        ).choices[0].message["content"]

        return response


class GPTCosplayTaskGenerator(GPTCosplay):
    """
    AI Teaching Assistant：
        generate feedback for courses according student attendance, quiz/assignment completion, etx
    """
    def __init__(self, topic, actor='question_generator'):
        super().__init__(actor=actor)
        self.topic = topic

    def process(self, api_key, model='gpt-3.5-turbo'):
        conjunction = 'Please generate one question related to topic: '

        messages = [{
            'role': 'user',
            'content': self.prompt + conjunction + '<' + self.topic + '>: '}]

        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model=model, messages=messages, temperature=0
        )
        result = response.choices[0].message["content"]
        return result


class GPTCosplayTaskReviewer(GPTCosplay):
    def __init__(self, question, answer, actor='python_code_reviewer'):
        super().__init__(actor=actor)
        self.question = question
        self.answer = answer

    def process(self, api_key, model='gpt-3.5-turbo'):
        mark_standard = ('Provide a mark from 1-100, 100 is awesome, and 0 is bad. '
                         'Answer with a format like ""Mark: 90/100, Comment: "". ')
        qa_conjunction = 'Please help to review the answer of the question: '

        messages = [{
            'role': 'user',
            'content': self.prompt + mark_standard + qa_conjunction +
                       'Question: ' + self.question + '\nAnswer: ' + self.answer}]

        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model=model, messages=messages, temperature=0
        )
        result = response.choices[0].message["content"]

        mark = re.findall("Mark[\s:]*(\d{,3}/100)\D", result)[0]
        comment = result.split('Comment: ')[1]

        return mark, comment


class GPTCosplayCourseFeedbackGenerator(GPTCosplay):
    def __init__(self, actor='course_feedback_generator'):
        # TODO: AI Teaching Assistant：
        #  generate feedback for courses according student attendance, quiz/assignment completion, etx
        super().__init__(actor=actor)


class GPTCosplayMessageMoralHazardReview(GPTCosplay):

    def __init__(self, actor='moral_hazard_reviewer'):
        # TODO: AI Teaching Assistant：
        #  moral hazard review of messages posted in forum, chatroom.S
        super().__init__(actor=actor)

