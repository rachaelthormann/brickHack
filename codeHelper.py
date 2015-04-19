# import necessary modules
from flask import Flask, request, redirect
from codeHelper_util import *
import twilio.twiml

"""
User sends a sms message via phone, and the same message
is sent back via twilio client.

date: 4/18/2015
filename: codeHelper.py
authors: Philip Bedward, Rachael Thormann and Qadir Haqq
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
    Sends a preset response back to the user when a reply is received.

    :return: the predetermined response
    """

    # enables this variable to be a response
    resp = twilio.twiml.Response()

    # sets the message equal to the body of the message the user sent
    message = request.form["Body"]
    if message == "Code help":
        categories = ["loops", "conditions", "arithmetic", "boolean logic"]
        initialResp(resp)
    elif message == "Loops":
        loopPrompt(resp)

    elif message == " Conditions":
        conditionsPrompt(resp)
    elif message == "Arithmetic":
        arithmtetic(resp)
    elif message == "Boolean Logic":
        bool(resp)
    elif message == "For" or message == "While":
        loopsResponse(resp,message)
    elif message == "Got help":
        finalResponse(resp)
    # sends the response back to user
    return str(resp)




if __name__ == "__main__":
    app.run(debug=True)