import requests
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)


@app.route("/login", methods = ["GET", "POST"])
def login():
    error = None
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        if request.form["uname"] != "admin" or request.form["password"] != "1234":
            error = "Invalid Credentials. Please try again."
        	# return render_template("login.html", error = error)
            return redirect(url_for("login"))
        else:
            return redirect(url_for("search"))
        # return render_template("login.html", error = error)

@app.route("/main", methods = ["GET", "POST"])
def search():
	if request.method == "GET":
		return render_template("main.html")
	elif request.method == "POST":
		information = get_information(request.form["search_word"])
		return render_template("main.html", information = information)
	
def get_information(search_word):
	req = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=&exsentences=2&explaintext=&redirects=&format=json&formatversion=2&titles=" + search_word)
	return req.json()['query']['pages'][0]['extract']