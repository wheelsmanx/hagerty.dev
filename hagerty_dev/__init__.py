from flask import Flask
app = Flask(__name__)

from datetime import datetime
from flask import render_template


@app.route("/")
def hello():
    return render_template('index.html')
	
	
	
if __name__ == "__main__":
    app.run('0.0.0.0')
