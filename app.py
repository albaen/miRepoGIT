from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hello"
    
@app.route('/health')
def health():
    return "200"

app.run(host='0.0.0.0', port='8080')