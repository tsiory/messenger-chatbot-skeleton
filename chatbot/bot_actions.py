from chatbot.fb_graph_api import send_api

send_api = send_api.SendApi("<YOUR_PAGE_TOKEN>")

##################################################################
# METTRE ICI LES CONTENUS PERSONNALISEES QUE PEUT ENVOYER LE BOT #
##################################################################
def seen(recipient_id):
	return send_api.mark_seen_message(recipient_id)

def typing_on(recipient_id):
	return send_api.typing_on_message(recipient_id)

def reply(recipient_id):
	return send_api.send_text_message("RESPONSE" , recipient_id , "<REPLY_MESSAGE>")