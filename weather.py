from flask import Flask,render_template,request
from local_settings import SECRET_KEY
import requests

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route("/city", methods=("GET", "POST"))
def get_weather():
    if request.method == "POST":
        city=request.form["city"]

        url_path = (
            'https://api.openweathermap.org/data/2.5/weather?q='
            +city
            +'&units=metric'
            +'&appid='
            +SECRET_KEY)
    
        r=requests.get(url_path)
        data=r.json()
        return render_template("index.html", city=city, data=data)

    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True,port=5001)
