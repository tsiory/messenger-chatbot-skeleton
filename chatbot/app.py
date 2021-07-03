from flask import Flask, request
from chatbot import bot

flask_app = Flask(__name__)

APP_SECRET = "<YOUR_APP_SECRET>"

# VERIFICATION DU TOKEN DE L'APP
@flask_app.route('/webhook', methods=['GET'])
def verify_token():
	verify_token = request.args.get("hub.verify_token")
	# Check if sent token is correct
	if verify_token == APP_SECRET:
		# Responds with the challenge token from the request
		return request.args.get("hub.challenge")
	return "Unable to authorise."


# GERE LES REQUETES POST (MESSAGE RECU)
@flask_app.route("/webhook" , methods=["POST"])
def handle_post_requests():
	request_content = request.get_json()
	
	bot_instance = bot.Bot("<YOUR_PAGE_TOKEN>")
	bot_instance.start(request_content)

	return "" , 200