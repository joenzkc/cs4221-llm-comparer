from flask import Flask, render_template, request, jsonify
from app.db import get
from app.llms.openai import generate_ai_response
from app.llms.claude import generate_claude_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['message']
        response = generate_response(user_input)
        return render_template('index.html', response=response)
    return render_template('index.html', response='')

def generate_response(user_input):
    # Your logic to generate a response based on user_input
    # run sql query
    # gpt response
    # result = generate_ai_response(user_input)

    # clause response
    claude_result = generate_claude_response(user_input)


    return f' \n Claude response: {claude_result}'

@app.route('/generate_dll', methods=['GET', 'POST'])
def generate_dll_page():
    if request.method == 'POST':
        user_input = request.json.get('requirements')

        result = generate_ai_response(user_input)
        return jsonify({
            'openai': result,
            'claude': ''
        })
    return render_template('generate_dll.html')
