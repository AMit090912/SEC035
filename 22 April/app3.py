from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

votes = {"cats": 0, "dogs": 0}

@app.route('/')
def index():
    return render_template_string(open("templates/index3.html", encoding='utf-8').read())

@app.route('/vote/<animal>', methods=['POST'])
def vote(animal):
    if animal in votes:
        votes[animal] += 1
    return jsonify(votes)

@app.route('/results', methods=['GET'])
def results():
    return jsonify(votes)

if __name__ == '__main__':
    app.run(debug=True)
