from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route("/")
def main():
    raw_data = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=e8a201e0")
    movies = raw_data.json()
    return render_template("home.html", movies=movies)



if __name__ == "__main__":
    app.run(debug=True)
