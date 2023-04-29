import pandas as pd
import numpy as np
import pickle

from surprise import Dataset, Reader
from surprise.model_selection import cross_validate
from surprise.prediction_algorithms import SVD
from surprise.model_selection import GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity


def recommendation_temp (userId, title):
    ratings = 'ratings.csv'
    index_map= 'index_map.csv'
    indices = 'indices.csv'
    links_map = 'links_map.csv'
    tmdb_data = 'tmdb_data.csv'
    cosine_sim = pickle.load(open('cosine_sim.pkl','rb'))
    svd_model = pickle.load(open('svd.pkl','rb'))
    df_recommended = pd.DataFrame()
    idx = indices[title]
    tmdbId = links_map.loc[title]['id']
    movie_id = links_map.loc[title]['movieId']
    sim_scores = list(enumerate(cosine_sim[int(idx)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:26]
    movie_indices = [i[0] for i in sim_scores]
    movies = tmdb_data.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'release_date', 'Film_director', 'id']]
    movies['rating'] = ratings['rating']
    movies['est'] = movies['id'].apply(lambda x: svd_model.predict(userId, index_map.loc[x]['movieId']).est)
    movies = round(movies.sort_values('est', ascending=False),2)
    return movies.head(10)

recommendation_temp(199, "The Terminator")





