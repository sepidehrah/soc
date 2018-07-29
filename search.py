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
            return redirect(url_for("login"))
        else:
            return redirect(url_for("search"))
        return render_template("login.html", error = error)

@app.route("/main", methods = ["GET", "POST"])
def search():
	if request.method == "GET":
		return render_template("main.html")
	elif request.method == "POST":
		return get_information(request.form["search_word"])
	
def get_information(search_word):
	req = requests.get("https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=" + search_word)
	page_id = list(req.json()['query']['pages'].keys())[0]
	print('THIS IS PAGE ID', page_id)
	return req.json()['query']['pages'][page_id]['extract']