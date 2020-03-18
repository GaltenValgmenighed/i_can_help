from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import pprint
import json
import time;
pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)
Bootstrap(app)

def save_data(data, outputfolder):
    ts = str(time.time())
    output = json.dumps(data)
    file = open(outputfolder + ts + '.txt', 'w')
    file.write(str(output))
    file.close()


@app.route('/')
def index():
     return render_template('index.html')

@app.route('/helpee', methods=['GET', 'POST'])
def parse_request_helpee():
    data = request.form
    print(request.form['name'])

    save_data(data, 'helpee/')
    return render_template('tak.html')

@app.route('/helper', methods=['GET', 'POST'])
def parse_request_helper():
    data = request.form

    save_data(data, 'helper/')
    return render_template('tak.html')



if __name__ == '__main__':
    app.run()
