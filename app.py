import os
import slack_sdk as slack
from slack_sdk import WebClient
from flask import Response, Flask, request

token=os.environ.get("SLACK_BOT_TOKEN")

client=slack.WebClient(token)

app = Flask('')

@app.route("/slack/commands", methods=['POST'])
def meet():

    new_meeting_url='http://meet.google.com/new'
    named_meeting_url='http://g.co/meet/'

    data = request.form
    slack_channel_id = data.get('channel_id')
    meeting_name = data.get('text')

    if meeting_name == "":
        client.chat_postMessage(channel=slack_channel_id, text=new_meeting_url)
        return Response(), 200
    else:
        client.chat_postMessage(channel=slack_channel_id, text=named_meeting_url+meeting_name.)
        return Response(), 200


# Start your app
if __name__ == "__main__":
    app.run('0.0.0.0', 3000, debug=True)
