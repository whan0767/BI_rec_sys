import pickle
import pandas as pd
from app import item_stat_matrix

def gen_user_item_seq(item_id,playtimes):
    return

def playtime2rating_norm(item_id, playtime):
    mean = item_stat_matrix.loc[item_id,('playtime_log','mean')]
    std = item_stat_matrix.loc[item_id,('playtime_log','std')]
    rating = (playtime - mean)/std
    return rating
