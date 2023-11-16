import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    secret_key = os.environ.get('OPENAI_SECRET_KEY');
    return 'Welcome to my website!'

if __name__ == '__main__':
    app.run()

