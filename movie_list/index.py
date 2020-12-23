from flask import Flask, render_template,request, url_for, redirect, session
import requests

app = Flask(__name__)
app.secret_key = "ftutd56d546hgjk"

@app.route("/")
def main():
    raw_data = requests.get("http://www.omdbapi.com/?apikey=e8a201e0&s=batman")
    movie_ids = raw_data.json()
    return render_template("home.html", movie_ids=movie_ids)
         
@app.route("/get_movie_details/<title>")
def get_movie_details(title):
    raw_data = requests.get("http://www.omdbapi.com/?apikey=e8a201e0&t="+title)
    movie_detail_ids = raw_data.json()
    return render_template("movie_details.html", movie_id=movie_detail_ids)

@app.route("/add_to_favorite/<title>")
def add_to_favorite(title):
    favorite_ids = {}
    if "favorite" in session:
        favorite_ids = session.get("favorite")
    else:
        session["favorite"] = {}
    favorite_ids[title] = title
    session["favorite"] = favorite_ids
    return redirect(url_for("main"))

@app.route("/search_by_title", methods=["POST"])
def search_by_title():
    title = request.form["title"]
    data_list = title.split(sep=':')
    search_ids = False
    if len(data_list) > 1:
        year = data_list[1]
        name = data_list[0]
        raw_data = requests.get("http://www.omdbapi.com/?apikey=e8a201e0&t="+name+"&y="+year)
        search_ids = raw_data.json()
    else:
        raw_data = requests.get("http://www.omdbapi.com/?apikey=e8a201e0&t="+title)
        search_ids = raw_data.json()

    print(len(search_ids))
    return render_template("search.html", search_id=search_ids)

if __name__ == "__main__":
    app.run(debug=True)

