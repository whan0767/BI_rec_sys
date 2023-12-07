import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import linear_kernel,cosine_similarity

def cal_cos_sim(item_seq):
    scaler = StandardScaler()
    numeric_features=scaler.fit_transform(item_seq.iloc[:,1:24])
    cosine_sim = cosine_similarity(numeric_features, numeric_features)
    return cosine_sim
    
def get_contents_recommendations(item_seq,cosine_sim,id):
    idx = item_seq[item_seq['id'] == id].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    #sim_scores = sim_scores[1:4]  # Exclude the item itself and get top 3
    item_indices = [i[0] for i in sim_scores[1:4]]
    return item_seq['app_name'].iloc[item_indices]