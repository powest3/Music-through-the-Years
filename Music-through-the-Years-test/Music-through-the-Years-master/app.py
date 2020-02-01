from flask import (
    Flask,
    render_template,
    jsonify)
from flask_pymongo import PyMongo
import pandas as pd

app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/billboard_db")
music = mongo.db.all_number_one_songs

#set the routes and render remplates for all the html files
# @app.route("/")
# def index():

@app.route("/")
def index():

    return render_template("Index.html")

@app.route("/Song.html")
def artist():

    return render_template("Song.html")

@app.route("/Artist-Comp.html")
def artistcomp():

    return render_template("Artist-Comp.html")

@app.route("/Song.PNG")
def songimg():

    return render_template("Song.PNG")

@app.route("/song_count")
def artist_count_data():
    
    # Query for the emoji data using pandas
    df = pd.DataFrame(list(music.find()))
    df['Length'] = df['issue_date'].str.len()
    df = df.sort_values(by='Length', ascending=False)
    df = df.head(10)
    # Format the data for Plotly
    trace = {
        "x": df["title"].values.tolist(),
        "y": df["Length"].values.tolist(),
        "type": "bar"
    }
    return jsonify(trace)



if __name__ == "__main__":
    app.run(debug=True)