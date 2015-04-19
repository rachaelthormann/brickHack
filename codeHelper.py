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
    # *For All:
    # checks the message the user sent and sets the response message based on
    # the user's reply
    if message == "Code help":
        #categories = ["loops", "conditions", "arithmetic", "boolean logic"]
        initialResp(resp)
    elif message == "Loops":
        loopPrompt(resp)
    elif message == "For" or message == "While":
        loopsResponse(resp,message)
    elif message == "Conditions":
        conditionsPrompt(resp)
    elif message in conditions_list:
        conditionsResponse(resp,message)
    elif message == "Arithmetic":
        arithmetic(resp)
    elif message == "Boolean logic":
        bool(resp)
    elif message in bools:
        boolResponse(message,resp)
    elif message == "Got help":
        finalResponse(resp)
    # sends the response back to user
    return str(resp)




if __name__ == "__main__":
    app.run(debug=True)