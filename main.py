# Import necessary libraries
from flask import Flask, request, jsonify
import random
import json
from flask_ngrok import run_with_ngrok
import random
import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

import openai
code = 'API'
openai.api_key = code

def askBert(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='answer as a person if this question about turism or travel otherwise just answer more than 2 sentences: ' +question,
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Ask a question




# Initialize the Flask app
app = Flask(__name__)

# Define a route for the root URL
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the VRGEN APP!"
@app.route('/salom', methods=['GET'])
def hello():
    return "Welcome to the VRGEN APP!"


# Define a route for GET request
@app.route('/get_data', methods=['GET'])
def get_example():
    data = request.get_json()
    random_number = random.randint(1, 10)
    if random_number % 5 == 0:
        rand = True
    else:
        rand = False
    pattern = {'question': data, 'answer': askBert(data), 'question_from_user': rand,"questionFromUserTexT":'question'}
    # Return response with the received data
    return jsonify(pattern)



    #http://localhost:5000/get_example?data=salom
    # Return response with the received data




# Define a route for POST request
@app.route('/post_example', methods=['POST'])
def post_example():
    # Get JSON data from request
    data = request.get_json()
    random_number = random.randint(1, 10)
    if random_number % 5 == 0:
        rand = True
    else:
        rand = False
    pattern = {'question': data, 'answer': askBert(data), 'question_from_user': rand,"questionFromUserTexT":'question'}
    # Return response with the received data
    return jsonify(pattern)


# Run the Flask app
if __name__ == '__main__':
    app.run()
