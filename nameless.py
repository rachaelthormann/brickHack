from Flask import Flask, request, redirect
import twilio.twiml
__author__ = 'Phil'
__author__ = 'Rachael'

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""

    from_number = request.values.get('From', None)
    message = "At a hackathon testing "

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


