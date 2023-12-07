from flask import Flask, render_template, request, jsonify
import json
import pickle
import pandas as pd
from utils.models import cal_cos_sim,get_contents_recommendations
app = Flask(__name__)

def load_data():
    with open('data/iid_map.pkl','rb') as f:
        iid_map = pickle.load(f)
    with open('data/iid_rmap.pkl','rb') as f:
        iid_rmap = pickle.load(f)
    with open('data/item_stat_matrix.pkl','rb') as f:
        item_stat_matrix = pd.DataFrame(pickle.load(f))
    item_seq = pd.read_csv('data/processed_item_data.csv')
    return iid_map, iid_rmap,item_stat_matrix,item_seq

@app.route('/')
def main():
    return render_template('home.html')


@app.route('/submit', methods=['POST'])
def submit():
    json_data = request.get_json(force=True)
    play_type = json_data['buttonClicked']
    items = json_data['input1'], json_data['input2'], json_data['input3']
    playtime = int(json_data['integerInput1']), int(json_data['integerInput2']), int(json_data['integerInput3'])
    
    res1 = get_contents_recommendations(item_seq,cosine_sim,int(iid_map[items[0]])).values.tolist()
    res2 = get_contents_recommendations(item_seq,cosine_sim,int(iid_map[items[1]])).values.tolist()
    if playtime[0]>playtime[1]:
        res = res1[0],res1[1],res2[0]
    else:
        res = res1[0],res2[0],res2[1]
    return jsonify({'game1': res[0], 'game2': res[1], 'game3': res[2]})


if __name__ == "__main__":
    iid_map, iid_rmap,item_stat_matrix,item_seq = load_data()
    cosine_sim = cal_cos_sim(item_seq)
    app.run(debug=True)

