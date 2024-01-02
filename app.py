from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import chatBot

app = Flask(__name__)
CORS(app)


@app.route('/ask_bot', methods=['POST'])
def ask():
    print(request.json)
    if 'messages' in request.json:
        query = request.json['messages'][0]["content"]
        print(query)
        res = chatBot.processPrompt(query)
        # Process the text and return a response
        return jsonify({'question': query, 'answer': res["answer"]})
    else:
        return {'error': 'No text provided in the request'}, 400  # Return a 400 Bad Request error

@app.route('/count_characters', methods=['POST'])
def count_characters():
    data = request.json
    text = data.get('text', '')
    character_count = len(text)
    return jsonify({'character_count': character_count})   

#@app.route('/ask', methods=['POST'])
#def ask():
#    text = request.json['text']
#    print(text)
    #choices = processResponse.processPrompt(text)
    #choices = llm("Q: " + text + " ? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)
    #return {'choices': choices}

@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host="0.0.0.0",use_reloader=False)

flask_cors.CORS(app, expose_headers='Authorization')



# edit the above flask app you wrote to: 

# 1. receive a payload of text
# 2. pass the text to the `text` argument in the following `llm` function shown here: llm("Q: " + text + " ? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)
# 3. assuming the output is an array called `choices` return that array as a response
