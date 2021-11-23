from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/post', methods = ['POST'])
def post_data():
    # POST endpoint to capture domain/category/value metric
    pass

@app.route('/get', methods = ['GET'])
def get_data():
    # GET endpoint to show values for a given domain
    pass

if __name__ == '__main__':
    app.run()
