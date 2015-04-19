import twilio.twiml
__author__ = 'Philip Bedward'
__author__ = 'Rachael Thormann'

def initialResp(resp):
    categories = ["loops", "conditions"]
    # makes response the body of the message that the user sent in
    response = "What category do you need help with?\n"
    for ch in categories:
        response += ch+"\nor\n"
    resp.message(response)

def loopPrompt(resp):
    response = "A for loop or a while loop?\n" \
                   "(Enter: 'for' -> for loop \nor\n" \
                   "'while' -> while loop).)"
    resp.message(response)

def loopsResponse(resp,message):
    response = loops(message)
    resp.message(response)

def loops(keyword):
    loops = ['For', 'While']
    if keyword in loops:
        if keyword == loops[0]:
            string = "What type of for loop?\n" \
                "For each loop or for loop through a range of number?"
        elif keyword == loops[1]:
            string = "What type of while loop?\n" \
                "While loop through a list or while loop through a range of number?"
        return string

