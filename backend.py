from flask import Flask, render_template, redirect, url_for, request
import csv
from flask.helpers import url_for
import pandas as p
import matplotlib
from datetime import datetime as dt
from matplotlib import pyplot as plt

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route('/data',methods=['GET','POST'])
def data():
    df = p.read_csv("static/Data Set - Insurance Client.csv")
    return render_template("index.html",data=df)

@app.route('/graph',methods=['GET','POST'])
def graph():
    file = "static/Data Set - Insurance Client.csv"
    fields = ["Policy_id","Date of Purchase"]
    g = p.read_csv(file, usecols=fields)
    g["Date of Purchase"] = p.to_datetime(g["Date of Purchase"])
    fig, ax = plt.subplots(figsize=(10,5))
    g.groupby(g["Date of Purchase"].dt.strftime('%b %Y'))["Policy_id"].count().plot(ax=ax)
    plt.show()
    fig.savefig('graph.png')
    return render_template("index.html")
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)