# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

from flask import Flask, request, redirect
import twilio.twiml
__author__ = 'Phil'
__author__ = 'Rachael'

app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])
def send_sms():
    resp = twilio.twiml.Response()
    message = request.form["Body"]
    resp.message(message)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)