import os
from flask import Flask, current_app, render_template, request, jsonify, Blueprint
from dotenv import load_dotenv
from app.db import get
from app.llms.claude import ClaudeClient
from app.llms.openai import OpenAIClient
from app.llms.BaseLLM import BaseLLM

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['message']
        response = current_app.claude.generate_response(user_input)
        return render_template('index.html', response=response)
    return render_template('index.html', response='')

def generate_response(user_input):
    # Your logic to generate a response based on user_input
    # run sql query
    # gpt response
    # result = generate_ai_response(user_input)

    # clause response
    claude_result = current_app.claude.generate_response(user_input, None)
    
    return f'\nClaude response: {claude_result}'

@main.route('/compare_llms', methods=['GET', 'POST'])
def compare_llms():
    return render_template('compare_llms.html')

@main.route('/response', methods=['POST'])
def generate_response():
    model = request.json.get('model', '')
    prompt = request.json.get('prompt', '')
    content_prompt = request.json.get('content_prompt', '')
    kwargs = request.json.get('args', {})

    client: BaseLLM = None
    if not model:
        return jsonify({'success': False, 'message': 'No model provided'})
    elif not (client := getattr(current_app, model)):
        return jsonify({'success': False, 'message': 'Model not valid'})
    elif not prompt:
        return jsonify({'success': False, 'message': 'Prompt must be provided'})
    
    return jsonify({
        'success': True,
        'message': client.generate_response(prompt, content_prompt, **kwargs)
    })

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)

    load_dotenv()
    required_env_vars = ['CLAUDE_API_KEY', 'OPENAI_API_KEY']
    for var in required_env_vars:
        env_var = os.environ.get(var)
        if not env_var:
            raise Exception(f"Missing env variable: {var}")
        app.config[var] = env_var

    with app.app_context():
        current_app.claude = ClaudeClient(app.config['CLAUDE_API_KEY'])
        current_app.openai = OpenAIClient(app.config['OPENAI_API_KEY'])
    
    return app