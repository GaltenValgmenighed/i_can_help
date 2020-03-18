from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import pprint
pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
     return render_template('index.html')

@app.route('/helpee', methods=['GET', 'POST'])
def parse_request_helpee():
    data = request.form
    print(request.form['name'])
    return jsonify(data)

@app.route('/helper', methods=['GET', 'POST'])
def parse_request_helper():
    data = request.form
    return jsonify(data)



if __name__ == '__main__':
    app.run()
