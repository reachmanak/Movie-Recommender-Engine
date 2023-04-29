from flask import render_template, request, jsonify,Flask
import flask
import numpy as np
import traceback #allows you to send error to user
import pickle
import pandas as pd


# App definition
app = Flask(__name__)

# importing models

from typing import Optional
from recommend import recommendation_temp


@app.get("/")
def read_root():
    return {"Status": "Working"}

@app.route('/')
def welcome():
   return "Welcome! Here you can get recommendation of movies based on your search"

@app.get("/recommendations")
def predict(userId: int, title: str):
    
    top_movies  = recommendation_temp(userId,title)
    top_movies  = list(top_movies)
    top_json = {"recommended":top_movies}
    
    return top_json

                

if __name__ == "__main__":
   app.run()

