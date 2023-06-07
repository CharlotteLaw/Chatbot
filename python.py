import openai
from flask import Flask, render_template, request
#from api_secrets import API_KEY

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    message = request.form['message']
    askprompt = "You are an informative, happy, and helpful personal assistant/chatbot. Chat with the user or answer their questions. " + message
    openai.api_key = "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"
    response = openai.Completion.create(engine="text-davinci-001", prompt=askprompt, max_tokens=100)
    resp = response.choices[0].text
    print(response)
    return render_template('index.html', m=message, r=resp)

if __name__ == '__main__':
    app.run(debug=True)

#openai.api_key = "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"

#askprompt = input("Say something to the chatbot: ")
#askprompt = message

#response = openai.Completion.create(engine="text-davinci-001", prompt=askprompt, max_tokens=6)

#print(response)
#print(response.choices[0].text)
# THE ABOVE WORKS
#print(response.choices[2].message)

#print(response[0][4])

#import os
#import openai
#openai.api_key = os.getenv("OPENAI_API_KEY")



#print(completion)