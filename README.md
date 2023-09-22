## Instruction
A Learning Management System will help faculty to better management admin, leaner, student, and includes AI teaching assistant.

## Highlight Features
AI Teacher Assistant includes 4 main functions: 
1. **Doc Recognition**: using OCR technology to read content from image and pdf into machine-readable format. It can quickly process digital document, no matter what study materials or assignment and the content can be saved for future use
2. **AI Generate Content**: based on a simple lesson description as prompt, LLM will give suggest quizzes and assignment questions. 
3. **Auto Review**: After assignment has been OCRed, TA chat robot can read and have a automatic review of code and give proper grades and comments. Teacher can choose to use or modified which would save massive redundant review work
4. **Forum collaboration**: our system contains a local knowledge-base with frequently asked questions, user can use Sentencebert model to match the student questions and answer from our knowledge-base. It will give proper answers when teacher is not available.
As the next step, we have three directions to optimize this function. We will add the Big model to review the forum content, filter out any discriminate words and identify plagiarism. Further more, we will introduce longchain +llm techniques for more AI TA functions and add our modules, references materials to ptuning the module to ensure the content is aligned.

## Setup with virtual environment

Setup a Python virtual environment (optional):
``` 
virtualenv .env
source .env/bin/activate
```

Install the requirements:
```
.env/bin/pip install -r requirements.txt
```

Download Sentence-bert model (model will be saved in `ai_teach_assist/models`):
```
python ai_teach_assist/faq_answer.py
```

Config ChatGPT API KEY `GPT_API_KEY` in `services/ai_service.py`

If everything works well, you can run `python main.py` to start service.


## TODO
AI Teaching Assistant:
1. generate feedback for courses according student attendance, quiz/assignment completion, etx
2. moral hazard review of messages posted in forum, chatroom.
3. ...