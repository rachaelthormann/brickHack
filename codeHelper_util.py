import twilio.twiml
"""
Holds all the utility methods that are to be used in codeHelper

date: 4/18/2015
filename: codeHelper_util.py
authors: Philip Bedward, Rachael Thormann and Qadir Haqq
"""
__author__ = 'Philip Bedward'
__author__ = 'Rachael Thormann'
__author__ = 'Qadir Haqq'

def initialResp(resp):
    categories = ["loops", "conditions", "arithmetic"]
    # makes response the body of the message that the user sent in
    response = "What category do you need help with?\n"
    for ch in categories:
        response += str.lower(ch+"\n")
        response = response.strip()
    resp.message(response)

def loopPrompt(resp):
    response = "A for loop or a while loop?\n" \
                   "(Enter: 'for' -> for loop \nor\n" \
                   "'while' -> while loop)."
    resp.message(response)

def loopsResponse(resp,message):
    response = loops(message)
    resp.message(response)

def loops(keyword):
    loops = ['For', 'While']
    if keyword in loops:
        if keyword == loops[0]:
            string = forLoops()
        elif keyword == loops[1]:
            string = whileLoops()
        return string

def forLoops():
    rang = "'to print the numbers 0 to 9:\n" \
             "'for i in range(0,10):'\n" \
             "  'print(i)'"
    each = "to print every element in a list:\n" \
           "'lst = [1,2,3]'\n" \
           "'for item in lst:'\n" \
           "    'print(item)'"
    forloops = rang + "\n\n"+each
    return forloops

def whileLoops():

    rang = "to print all elements 0 to 9:\n" \
           "'while i < 10:' -> stops when i is equal to 10\n" \
           "    'print(i)' -> prints the current \n" \
           "    'i = i + 1' -> makes i's new value equal to its current value plus one."

    access = "to print all elementa in a list:\n" \
             "'lst = [1,2,3]' -> create a list of the #s 1,2 & 3\n" \
             "'index = 0' -> all lists start at index 0\n" \
             "len() ->len is used to get the length of the list and/or string"\
             "'while index < len(lst):' ->  ->the last index is always equal to the length of the list minus one\n" \
             "'print(lst[index])'-> prints what is at that index "

    whileloops = rang + "\n\n" + access
    return whileloops

def conditionsPrompt(resp):
    response = "A if, elif, or else condition?\n" \
                "(Enter: 'if' -> if conditional \n,\n" \
                "'elif' -> elif conditional \nor\n" \
                "'else' ->  else conditional)."
    resp.message(response)

def conditionsResponse(resp, message):
    response = conditions(message)
    resp.message(response)

def conditions(keyWord):
    conditions = ['if', 'elif', 'else']
    if keyWord in conditions:
        if keyWord == conditions[0]:
            string = ""
        elif keyWord == conditions[1]:
            string = ""
        elif keyWord == conditions[2]:
            string = ""
        return string

def arithmetic(keyWord):
    operators = ["+", "-", "/", "//", "%", "*", "**"]
    if keyWord in conditions:
        if keyWord == conditions[0]:
            string = "+ is a binary operator that adds two elements in infix notation, EX: 5 + 4)"
        elif keyWord == conditions[1]:
            string = "- is a binary operator that subtracts two elements in infix notation, EX: 5 - 4. " \
                     "Can also be used with strings to take out the first occurrence of a letter, if the string" \
                     "contains that letter."
        elif keyWord == conditions[2]:
            string = "/ is a binary operator that divides two elements in infix notation, EX: 4/2. " \
                "If either element on the side is double, it converts the integer type to an double."
        elif keyWord == conditions[3]:
            string = "// is a binary operator that divides two elements in infix notation, EX: 5//2 = 2." \
                     "Returns an integer division, "
        elif keyWord == conditions[4]:
            string = ""
        elif keyWord == conditions[5]:
            string = ""
        elif keyWord == conditions[6]:
            string = ""
        return string

def arithmeticResponse(resp, message):
    response = arithmetic(message)
    resp.message(response)