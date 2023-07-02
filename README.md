# Chatbot
A personal chatbot and online assistant developed utilizing the GPT-3 open-source language model. 

## How it works

**Back End**  
* Programmed using Python 
* Used [Flask](https://flask.palletsprojects.com/) as a backend framework to retrieve user input and display chatbot output
* Integrated [MySQL](https://dev.mysql.com/doc/refman/8.0/en/what-is-mysql.html) to create a database to store user's messages and the chatbot's responses
* Integrated [OpenAI's GPT-3](https://platform.openai.com/docs/guides/gpt) open-source language model API using python to generate contextual responses  

**Front End**  
* Programmed using HTML and CSS  
* Used [Flask](https://flask.palletsprojects.com/) to return HTML and CSS as the web application


  
    
    
## How to Run Locally

1. Clone this repo
2. Download [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)
3. Run the following in MySQL Workbench to create a database


```MySQL
CREATE DATABASE messages
CREATE TABLE convo (ID int primary key, question VARCHAR(3000), response VARCHAR(3000));
```


5. Within MySQL Workbench, connect to the `messages` database
6. Edit the convo table to set ID to auto increment and click apply
7. Generate your own API key from [OpenAI](https://openai.com/) and replace it in the code within the `getvalue()` function  
8. Run `python.py`
9. Use browser to connect to [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/) to interact with chatbot  




  
**Disclaimer**  
As of now, I have implemented GPT-3 as an open-source language model and created a chatbot web application with a frontend and backend using the GPT-3 API. With more time, I would like to look into setting up a suitable deep learning framework with GPT-3. 


    
    
## Program Preview

<img width="1435" alt="image" src="https://github.com/CharlotteLaw/chatbot/assets/69742430/155f7055-6bd4-4b3e-a5dd-a167f23e7c3d">
