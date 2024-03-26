from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome! to the princess quiz.'

if __name__ == '__main__':
    app.run(host='localhost', port=7071)