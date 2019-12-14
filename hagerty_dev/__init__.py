from flask import Flask
from flask import request
from slackeventsapi import SlackEventAdapter
app = Flask(__name__)

from datetime import datetime
from flask import render_template

from github import Github
import json

from pymongo import MongoClient
import slack
import os 
import traceback
import re

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"

# Module: notABot.py





slack_events_adapter = SlackEventAdapter("", "/bots/notabot", app)
slack_client = slack.WebClient(token="")
    
@slack_events_adapter.on("member_joined_channel")
def handle_message(event_data):
    message = event_data["event"]
    # If the incoming message contains "hi", then respond with a "Hello" message
    channel = message["channel"]
    message = "Hello and welcome <@%s>! :tada:" % message["user"]
    slack_client.chat_postMessage(channel=channel, text=message)

# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    message = event_data["event"]
    emoji = message["reaction"]
    channel = message["item"]["channel"]
    message = "Hello loser <@%s>! :tada:" % message["user"]
    slack_client.chat_postMessage(channel=channel, text=message)

# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))


def databaseSetup():
	returnObject = ""
	client = MongoClient('localhost',27017)
	post = {"author": "Mike",
		"text": "My first blog post!",
		"tags": ["mongodb", "python", "pymongo"],
		"date": "12"}
	db = client['test-database']
	collection = db['test-collection']
	collection_id = collection.insert_one(post).inserted_id

	return db['test-collection']


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
	data = databaseSetup()
	return render_template('/test/index.html', data=map(json.dumps,data))
	

@app.route("/test/contactMe")
def test_contactMe():
	return render_template('/test/contactMe.html')
	
@app.route("/test/slackBots")
def test_slackBots():
	return render_template('/test/slackBots.html')
	
if __name__ == "__main__":
	app.run('0.0.0.0')
