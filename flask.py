from flask import Flask, jsonify, request
from flask_restful import Resource, Api
  
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)
  
# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
@app.route('/')
def welcome():
   return "Welcome! Here you can get recommendation of movies based on your search"

@app.route("/recms", methods = ["POST"])
class Final_Recommendations:
    def __init__(self):
        self.hist = []

def recommendation(userId, title):
    idx = indices[title]
    tmdbId = links_map.loc[title]['id']
    movie_id = links_map.loc[title]['movieId']
    sim_scores = list(enumerate(cosine_sim[int(idx)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:26]
    movie_indices = [i[0] for i in sim_scores]
    movies = tmdb_data.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'release_date', 'Film_director', 'id']]
    movies['rating'] = ratings['rating']
    movies['est'] = movies['id'].apply(lambda x: svd.predict(userId, index_map.loc[x]['movieId']).est)
    movies = round(movies.sort_values('est', ascending=False),2)
    self.hist.append(movies.head(10))
    return movies.head(10)
  
    # Corresponds to POST request
def post(self):
          
    data = request.get_json()     # status code
    return jsonify({'data': data}), 201
    