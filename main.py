from services import *
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.register_blueprint(auth)
app.register_blueprint(article)
app.register_blueprint(permission)
app.register_blueprint(course)
app.register_blueprint(record)
app.register_blueprint(role)
app.register_blueprint(user)
app.register_blueprint(quiz_mcq_bp)
app.register_blueprint(ai_service)


# Import and register blueprints for different services
from services.user_role_service import user_role_service_bp
from services.module_service import module_service_bp

app.register_blueprint(user_role_service_bp)
app.register_blueprint(module_service_bp)


@app.route('/')
def index():
    return 'welcome to hackathon webpage!'


if __name__ == "__main__":
    print("Starting hackathon backend")
    from waitress import serve
    # serve(app, port=8080)
    app.run(port=8080, host="127.0.0.1", debug=True)

