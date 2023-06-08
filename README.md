# Chatbot | How It Works

**Back End**  
• Programmed using Python  
• Used Flask as a backend framework to retrieve user input and display chatbot output   
• Integrated MySQL to create a database to store user's messages and the chatbot's responses  
• Integrated OpenAI's GPT-3 open-source language model API using python to generate contextual responses

**Front End**  
• Programmed using HTML and CSS
• Used Flask to return HTML and CSS as the web application


# How To Run The Program

1. Download the Python, CSS, and HTML files  
2. Download MySQL Workbench
3. Run the following in MySQL Workbench to create a database  
`CREATE DATABASE messages;`  
`CREATE TABLE convo (ID int primary key, question VARCHAR(3000), response VARCHAR(3000));`
4. Within MySQL Workbench, connect to the messages database. 
5. Set ID to auto increment and apply.
6. Generate your own API key from OpenAI
7. Run the python file
