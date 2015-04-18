# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

__author__ = 'Phil'
__author__ = 'Rachael'

# Find these values at https://twilio.com/user/account
account_sid = "ACb63800b54ab0a07ff095d2632e9755aa"
auth_token = "8ec0dc3798983cdb5888bdaa511cf958"
client = TwilioRestClient(account_sid, auth_token)

