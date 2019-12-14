from flask import Flask
app = Flask(__name__)

from datetime import datetime
from flask import render_template


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/contactMe")
def contactMe():
    return render_template('index.html')
	
@app.route("/slackBots")
def slackBots():
    return render_template('index.html')
	
@app.route("/test")
def test_home():
    return render_template('/test/index.html')

@app.route("/test/contactMe")
def test_contactMe():
    return render_template('/test/contactMe.html')
	
@app.route("/test/slackBots")
def test_slackBots():
    return render_template('/test/slackBots.html')
	
if __name__ == "__main__":
    app.run('0.0.0.0')
