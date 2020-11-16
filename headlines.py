from flask import flask
app =  Flask(__name__)

@app.route('/')
def hello():
    return "<h1> Aloha <h1>"
if __name__ == '__main__':
    app.debug()
