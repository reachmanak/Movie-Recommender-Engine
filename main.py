from typing import Optional
from fastapi import FastAPI
from recommend import recommendation_temp

app = FastAPI()


@app.get("/")
def read_root():
    return {"Status": "Working"}


# Input Type : GET /recommendations?songs=3,6,12
# Output Type: { "recommended": [ 30749, 48439, 82784, 144942, 176568 ] }

@app.get("/recommendations")
def predict(userId: int, title: str):
    
    top_movies  = recommendation_temp(userId,title)
    top_movies  = list(top_movies)
    top_json = {"recommended":top_movies}
    
    return top_json 