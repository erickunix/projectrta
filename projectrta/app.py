import flask
from flask import Flask, request, render_template


app=Flask(__name__)

@app.route("/")
def home():
    #return {"status":0}
    return render_template("v2.html")

if __name__=="__main__":
     app.run(port=8000,host='0.0.0.0')


