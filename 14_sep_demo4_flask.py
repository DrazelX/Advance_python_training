from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1> Hello World </h1>'

# dynamic route
# http:127.0.0.1/Ayush
# Hello Ayush

@app.route('/user/<name>')
def user(name):
    return 'Hello, %s' % name

# headers
@app.route("/headers")
def headers():
    user_agent = request.headers.get('User-Agent')
    return '<p> Your Browser is %s</p>' % user_agent

if __name__ == '__main__':
    app.run(debug=True)
