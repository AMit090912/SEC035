from flask import Flask, jsonify, render_template_string

app = Flask(__name__)
counter = {"value": 0}

@app.route('/')
def index():
    return render_template_string(open("templates/index2.html").read())

@app.route('/increment', methods=['POST'])
def increment():
    counter["value"] += 1
    return jsonify({"count": counter["value"]})

if __name__ == '__main__':
    app.run(debug=True)
