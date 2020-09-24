from flask import Flask
import time
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!TEST'

@app.route('/time')
def return_time():
    return time.strftime("%a %b %d %Y %H:%M:%S", time.gmtime())

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
