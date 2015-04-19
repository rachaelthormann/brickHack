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
bools = ["==","!=","Or","And","Not"]
conditions_list = ["If", "Elif","Else"]
byemsg = "Enter 'Got help' to exit"
def initialResp(resp):
    """
    The initial response to the user's first message

    :param resp: the response variable. Text will be stored her and sent back
    to the user
    :return:
    """



    categories = ["loops", "conditions", "arithmetic", "boolean logic"]

    response = "What category do you need help with?\n"
    # add every category to the response variable
    # separate each word using new-line characters
    for category in categories:
        response += str.lower(category)
        response = response.strip() +"\n"
    response += "\n\n"+byemsg
    resp.message(response)

def finalResponse(resp):
    """
    exiting message to the user.

    :param resp: the response variable. Text will be stored her and sent back
    to the user.

    :return:
    """
    final = "We hope you were helped with everything you needed." \
            "\n Bye bye."
    resp.message(final)

def loopPrompt(resp):
    """
    prompt the user to find out what kind of loop they are
    interested in.

    :param resp: the response variable. Text will be stored her and sent back
    to the user
    :return:
    """
    response = "A for loop or a while loop?\n" \
                   "(Enter: 'for' -> for loop \nor\n" \
                   "'while' -> while loop)." \
                   "\n\n "+byemsg
    resp.message(response)

def loopsResponse(resp,message):
    """
    set the response message

    :param resp: the response variable. Text will be stored her and sent back
    to the user
    :param message: The message that the user sent
    :return:
    """
    response = loops(message)
    resp.message(response)

def loops(keyword):
    """
    a certain set of examples is stored in string depending on what
    keyword the user entered

    :param keyword: The message the user entered
    :return: The message of examples back to the user.
    """
    loops = ['For', 'While']
    if keyword in loops:
        if keyword == loops[0]:
            string = forLoops()
        elif keyword == loops[1]:
            string = whileLoops()
        return string

def forLoops():
    """

    :return: a string of examples and explanations to be sent to the user
    if they are interested in learning about for loops.
    """
    rang = "To print the numbers 0 to 9:\n" \
           "range() -> built in function that takes a start and an end value; " \
           "the end value is exclusive\n" \
           "'for i in range(0,10):'->numbers between 0 through 9 inclusive\n" \
           "  'print(i)'-> prints the number"
    each = "To print every element in a list:\n" \
           "'lst = [1,2,3]'\n" \
           "'for item in lst:'\n" \
           "    'print(item)'"
    hint = "For loops, unlike while loops, iterate through things for you" \
           " so you do not have to increment i to go the next number, or do anything to" \
           " the lst to go to the next item."
    forloops = "Here are some examples - \n\n"+rang + "\n\n"+each +"\n"+hint+"\n\n"+byemsg
    return forloops

def whileLoops():
    """

    :return: a string of examples and explanations to be sent to the user
    if they are interested in learning about while loops.
    """
    rang = "To print all elements 0 to 9:\n" \
           "'while i < 10:' -> stops when i is equal to 10\n" \
           "    'print(i)' -> prints the current \n" \
           "    'i += 1' -> sets i equal to its current value plus one.\n"

    access = "To print all elements in a list:\n" \
             "'lst = [1,2,3]' -> Create a list of the #s 1,2 & 3\n" \
             "'index = 0' -> All lists start at index 0\n" \
             "len() ->len is used to get the length of the list and/or string"\
             "'while index < len(lst):' ->  ->The last index is always equal to the length of the list minus one\n" \
             "'print(lst[index])'-> Prints what is at that index "

    hint = "While loops, unlike for loops, do not iterate through things for you" \
           " so you do have to increment i to go the next number, or to" \
           " go to the next item in a list."

    whileloops = "Here are some examples - \n\n"+rang + "\n" + access +"\n"+hint+"\n\n"+byemsg

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

    if keyWord in conditions_list:
        if keyWord == conditions_list[0]:
            string = "'if' -> only gets through the statement if the condition evaluates to true.\n" \
                     "Example: \n" \
                     "'if n ==1:'\n" \
                     "      'print('one')'\n" \
                     "-> 'one' would be printed when n is equal to one\n\n"+byemsg
        elif keyWord == conditions_list[1]:
            string = "'elif' -> meaning otherwise if or else if.\nOnly gets through" \
                     " the check if the condition evaluates to true\n" \
                     "Example:\n" \
                     "'elif n ==2:'\n" \
                     "      'print('two')'\n" \
                     "-> 'two' would be printed when n is equal to two\n\n" +byemsg
        elif keyWord == conditions_list[2]:
            string = "'else' -> meaning if all preceding conditions are false then do this\n" \
                     "Example:\n" \
                     "'else:'\n" \
                     "  'print('another number')'\n" \
                     "-> 'another number' would be printed when n is not equal to 1 and 2 \n\n" +byemsg
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

def booleanPrompt(reply):

    prompt = "Which boolen operator would you like to know about?\n"
    for b in bools:
        prompt += b + "\n"
    prompt += "\n\n"+byemsg

    reply.message(prompt)

def booleanResponse(keyWord,reply):
    response = booleans(keyWord)
    reply.message(response)

def booleans(keyWord):
    if keyWord == bools[0]:
        string = doubleEquals()
    elif keyWord == bools[1]:
        string = notEquals()
    elif keyWord == bools[2]:
        string = orOp()
    elif keyWord == bools[3]:
        string = andOp()
    elif keyWord == bools[4]:
        string = negate()
    return string

def doubleEquals():
    ans = "'==' checks if two things are equal\n" \
          "Example: \n" \
          "'5 == 5 -> True because 5 is equal to 5\n" \
          "'5 == 4' -> False becuase 5 is not equal to 4\n"
    ans += "\n\n"+byemsg
    return ans

def notEquals():
    ans = "'!=' checks if two things are not equal\n" \
          "Example: \n" \
          "'5 != 5 -> False because 5 is equal to 5\n" \
          "'5 != 4' -> True becuase 5 is not equal to 4\n"
    ans += "\n\n"+byemsg
    return ans

def andOp():
    ans = "'and' Checks two conditions and it only evaluates to true if" \
          "both conditions are true.\n" \
          "Example:\n" \
          "'if 5==5 and 5 > 4:'\n" \
          "     'print('good job')'\n" \
          "-> 'good job' would be printed because both of those conditions are true\n\n"\
          "'if 5 == 5 and 5 < 4:'\n" \
          "     'print('good job')'\n" \
          "-> 'good job' would not be printed because the second condition is false\n"
    ans += "\n\n"+byemsg
    return ans

def orOp():
    ans = "'or' Checks two conditions and it evaluates to true if" \
          "only one condition is true.\n" \
          "Example:\n" \
          "'if 5==5 and 5 > 4:'\n" \
          "     'print('good job')'\n" \
          "-> 'good job' would be printed because both of those conditions are true\n\n"\
          "'if 5==5 and 5 < 4:'\n" \
          "     'print('good job')'\n" \
          "-> 'good job' would be printed because the first conditions is true\n\n"\
          "'if 5 != 5 and 5 < 4:'\n" \
          "     'print('good job')'\n" \
          "-> 'good job' would not be printed because the both conditions are false\n"
    ans += "\n\n"+byemsg
    return ans

def negate():
    ans = "not' negates the boolean value the proceeds it.\n" \
          "Example:\n" \
          "'if not 5 == 5:'\n" \
          "     'print('hello')'\n" \
          "-> This would not print hello because 5 ==5 is true, but this condition says\n" \
          " not 5==5 which evaluates to false\n" \
          "'if not 5 != 5:'" \
          "     'print('hello')'" \
          "-> This would print hello because 5 != 5 is false, but this condition says\n" \
          " not 5==5 which evaluates to true\n"
    ans += "\n\n"+byemsg
