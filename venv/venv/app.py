# app.py
from flask import Flask

#assert response.data == b'Hello, Devops!'

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, devops!"

if __name__ == "__main__":
    app.run(debug=True)
