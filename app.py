from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('home.html')


@app.route('/submit', methods=['POST'])
def submit():
    json_data = request.get_json(force=True)
    play_type = json_data['buttonClicked']
    items = json_data['input1'], json_data['input2'], json_data['input3']
    playtime = json_data['integerInput1'], json_data['integerInput2'], json_data['integerInput3']
    return jsonify({'game1': 'total war', 'game2': 'biped', 'game3': 'overwatch2'})


if __name__ == "__main__":
    app.run(debug=True)
