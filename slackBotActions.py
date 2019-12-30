#test modular import
#import requests 

def ifany(text,needle):
    for x in text:
        if(str(x).lower() == needle):
            return True
    return False

def slackParse(event_dump):
    returnObject = dict()
    returnObject['text'] = "A Very General Error"
    returnObject['unit'] = False
    actionType = event_dump["event"]["type"]
    if(actionType == "reaction_added"):
        returnObject['channel'] = event_dump["event"]["item"]["channel"]
        returnObject['text'] = "this is a test"
        returnObject['thread_ts'] = event_dump["event"]["item"]["ts"]
        returnObject['unit'] = True
    if(actionType == "member_joined_channel"):
        returnObject['channel'] = event_dump["event"]["channel"]
        returnObject['user'] = event_dump["event"]["user"]
        returnObject['text'] = "Welcome <@" + returnObject['user'] + ">!"
        returnObject['unit'] = True
    if(actionType == "message"):
        returnObject['channel'] = event_dump["event"]["channel"]
        #returnObject['user'] = event_dump["event"]["user"]
        returnObject['message'] = event_dump["event"]["text"]
        returnObject['thread_ts'] = event_dump["event"]["ts"]
        returnObject['unit'] = True
        returnObject['text'] = returnObject['message'][1:]
    return returnObject
	
