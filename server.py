from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session as browser_session
import requests

app = Flask(__name__)
	
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/work')
def work():
	return render_template("work.html")

@app.route('/impact')
def impact():
	return render_template("impact.html")

@app.route('/approach')
def approach():
	return render_template("approach.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/contact')
def contact():

	"""User writes info in login email    
	# boxes and clicks submit, which directs here"""
	
	# fname = request.form.get("fname")
	# lname = request.form.get("lname")
	# email = request.form.get("email")
	# phone = request.form.get("phone")

	return render_template("contact.html")
	
@app.route('/send-email', methods=['POST'])
def send_email():
	subject = request.form.get("subject")
	message = request.form.get("message")	
	return requests.post(
        "https://api.mailgun.net/v3/localhost:5000/messages",
        auth=("api", "key-fec8a53f71b9c7d3e1e811ce7a7b69ac"),
        data={"from": "Mailgun Sandbox <postmaster@localhost:5000>",
              "to": "J <jkgriffin234@gmail.com>",
              "subject": "{subject}".format(subject=subject),
              "text": "{message}".format(message=message)})

if __name__ == "__main__":
	app.debug = True

	connect_to_db(app)

	DebugToolbarExtension(app)

	app.run()
