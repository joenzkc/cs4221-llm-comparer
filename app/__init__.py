from flask import Flask, render_template, request
from app.db import get
from app.llms.openai import generate_ai_response

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
    result = generate_ai_response(user_input)


    return f'{result}'
