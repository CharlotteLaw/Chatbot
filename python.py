import openai
from flask import Flask, render_template, request
import mysql.connector
#from api_secrets import API_KEY

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Charlotte19!",
    database="messages"
)

mycursor = db.cursor()

mycursor.execute("SELECT * FROM Conversations")

for x in mycursor:
    print(x)

#mycursor.execute("CREATE DATABASE messages")
#mycursor.execute("CREATE TABLE Conversations (question VARCHAR(300), response VARCHAR(300))")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    message = request.form['message']
    askprompt = "You are an informative, happy, and helpful personal assistant/ AI chatbot. Chat with the user or answer their questions. The user says: " + message
    openai.api_key = "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"
    response = openai.Completion.create(engine="text-davinci-001", prompt=askprompt, max_tokens=200)
    resp = response.choices[0].text
    print(response)
    mycursor.execute("INSERT INTO Conversations (question, response) VALUES (%s, %s)", (message, resp))
    db.commit()
    return render_template('index.html', m=message, r=resp)


if __name__ == '__main__':
    app.run(debug=True)

