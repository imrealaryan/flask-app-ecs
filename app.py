from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'My name is Aryan Jain and I am a DevOps Engineer with a passion of making my own projects'

@app.route('/health')
def health():
    return 'Server is up and running'
