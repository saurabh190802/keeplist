from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'saurabh'

@app.route('/12')
def hello():
    return 'saurabh satapathy'

@app.route('/21')
def hello_w():
    return 'sauragvedgiwegibh'

if __name__ == "__main__":
    app.run(debug=True)