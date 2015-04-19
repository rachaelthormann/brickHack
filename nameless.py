# import necessary modules
from flask import Flask, request, redirect
from stuff import *
import twilio.twiml

"""
User sends a sms message via phone, and the same message
is sent back via twilio client.

date: 4/18/2015
filename:
authors: Philip Bedward and Rachael Thormann
"""

__author__ = 'Philip Bedward'
__author__ = 'Rachael Thormann'
__author__ = 'Qadir Haqq'

# sets a variable for the constructor and module for this file
app = Flask(__name__)

# sets the URL rule endpoint to /sms
# limits the URL to the methods GET and POST
@app.route("/sms", methods=['GET', 'POST'])

def send_sms():
    """
    Sends the same sms message back to a user that is
    sent in to the twilio client.

    :return: the echoed response
    """

    # enables this variable to be a response
    resp = twilio.twiml.Response()

    # sets the message equal to the body of the message the user sent
    message = request.form["Body"]
    if message == "Code help":
        categories = ["loops", "conditions", "arithmetic", "boolean logic"]
        # makes response the body of the message that the user sent in
        initialResp(resp)
    elif message == "Loops":
        loopPrompt(resp)
    elif message == "Conditions":
        conditionPrompy(resp)
    elif message == "Arithmetic":
        arithmtetic(resp)
    elif message == "Boolean Logic":
        bool(resp)
    else:
        loopsResponse(resp,message)

    # sends the response back to user
    return str(resp)




if __name__ == "__main__":
    app.run(debug=True)